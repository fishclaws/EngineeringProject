from django.shortcuts import get_object_or_404, render
from django import forms
from django.http import HttpResponseRedirect
from .models import FeatureRequest
from .models import Client
from .models import ProductArea
from .forms import FeatureRequestForm

def index(request):
    request_list = FeatureRequest.objects.order_by('-client_priority')[:100]
    context = {'feature_request_list' : request_list}
    return render(request, 'feature_requests/index.html', context)

def detail(request, feature_request_id):
    feature_request = get_object_or_404(FeatureRequest, pk=feature_request_id)
    return render(request, 'feature_requests/detail.html', {'request': feature_request})

def delete(request, feature_request_id):
    request = FeatureRequest.objects.get(pk=feature_request_id)
    request.delete()
    return HttpResponseRedirect('../../index')

def addTestData(request):
    for letter in ('A', 'B', 'C'):
        if not Client.objects.filter(name = "Client " + letter).exists():
            client = Client(name = "Client " + letter)
            client.save()
    for product_name in ('Policies', 'Billing', 'Claims', 'Reports'):
        if not ProductArea.objects.filter(product_category = product_name).exists():
            pa = ProductArea(product_category = product_name)
            pa.save()
    return HttpResponseRedirect('../index')

def new(request):
    if request.method == 'POST':
        print("posting")
        form = FeatureRequestForm(data = request.POST)
        if form.is_valid():
            feature_request = form.save(commit=False)
            feature_request.correctClientPriorities()
            feature_request.save()
            return HttpResponseRedirect('../index')
        else:
            print(form.errors)
    else:
        form = FeatureRequestForm()
    return render(request, 'feature_requests/new.html',
    {
    'form': form,
    'client_list': Client.objects.all(),
    'product_area_list' : ProductArea.objects.all()
    })
