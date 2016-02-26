from django.shortcuts import get_object_or_404, render
from django import forms
from django.http import HttpResponseRedirect
from .models import FeatureRequest
from .models import Client
from .models import ProductArea
from .forms import FeatureRequestForm
from .forms import FeatureRequestDescriptionForm

#Views accessible by app

#renders list of feature requests ordered by client priority (max 100)
def index(request):
    request_list = FeatureRequest.objects.order_by('-client_priority')
    context = {'feature_request_list' : request_list}
    return render(request, 'feature_requests/index.html', context)

#renders a page with the description of the request
def detail(request, feature_request_id):
    feature_request = get_object_or_404(FeatureRequest, pk=feature_request_id)
    return render(request, 'feature_requests/detail.html', {'request': feature_request})

#edits description
def edit(request, feature_request_id):
    error_text = ""
    if request.method == 'POST':
        form = FeatureRequestDescriptionForm(data = request.POST)
        if form.is_valid():
            update_request = form.save(commit = False)
            feature_request = FeatureRequest.objects.get(pk = feature_request_id)
            feature_request.description = update_request.description
            feature_request.save()
            return HttpResponseRedirect('../../index')
        else:
            print (form.errors)
            error_text = form.errors
    else:
        form = FeatureRequestForm(instance = get_object_or_404(FeatureRequest, pk=feature_request_id))
    return render(request, 'feature_requests/detail.html',
    {
    'request': form,
    'error_text' : error_text
    })

#removes feature request
def delete(request, feature_request_id):
    request = FeatureRequest.objects.get(pk=feature_request_id)
    request.delete()
    return HttpResponseRedirect('../../index')

#posts test data as requested by the app specifications to the DB if it does not exist
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

#renders a form to create a new request
def new(request):
    error_text = ""
    if request.method == 'POST':
        form = FeatureRequestForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../index')
        else:
            print (form.errors)
            error_text = form.errors
    else:
        form = FeatureRequestForm()
    return render(request, 'feature_requests/new.html',
    {
    'form': form,
    'client_list': Client.objects.all(),
    'product_area_list' : ProductArea.objects.all(),
    'error_text' : error_text
    })
