from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django import forms
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from .models import FeatureRequest
from .models import Client
from .models import ProductArea
from .forms import FeatureRequestForm
from .forms import FeatureRequestDescriptionForm
from .exceptions import ConcurrentModificationError

#renders list of feature requests ordered by client priority (max 100)
def index(request):
    request_list = FeatureRequest.objects.order_by('-client_priority')
    context = {'feature_request_list' : request_list, 'current_user' : request.user}
    return render(request, 'feature_requests/index.html', context)

#edits description
@login_required(login_url='/feature_requests/login/')
def editDescription(request, feature_request_id):
    error_text = ""
    if request.method == 'POST':
        form = FeatureRequestDescriptionForm(data = request.POST, instance = FeatureRequest.objects.get(pk = feature_request_id))
        if form.is_valid():
            try:
                fr = form.save(commit = False)
                if fr.user == request.user:
                    fr.save()
                    return HttpResponseRedirect('../../')
                else:
                    error_text = "You do not have permission edit this request."
            except ConcurrentModificationError as e:
                error_text = e.message
        else:
            print (form.errors)
            error_text = form.errors
    else:
        form = FeatureRequestForm(instance = get_object_or_404(FeatureRequest, pk=feature_request_id))
    print(form)
    return render(request, 'feature_requests/detail.html',
    {
    'request': form,
    'feature_request_id' : feature_request_id,
    'error_text' : error_text
    })

#renders a form to create a new request
#posts the form
@login_required(login_url='/feature_requests/login/')
def new(request):
    error_text = ""
    if request.method == 'POST':
        form = FeatureRequestForm(data = request.POST)
        if form.is_valid():
            fr = form.save(commit = False)
            fr.user = request.user
            fr.save()
            return HttpResponseRedirect('../')
        else:
            print (form.errors)
            error_text = form.errors
    else:
        form = FeatureRequestForm()
    return render(request, 'feature_requests/edit.html',
    {
    'form': form,
    'client_list': Client.objects.all(),
    'product_area_list' : ProductArea.objects.all(),
    'error_text' : error_text
    })

#renders a form to edit the existing request
#posts the form
@login_required(login_url='/feature_requests/login/')
def edit(request, feature_request_id):
    error_text = ""
    if request.method == 'POST':
        form = FeatureRequestForm(data = request.POST, instance=FeatureRequest.objects.get(pk = feature_request_id))
        if form.is_valid():
            try:
                fr = form.save(commit = False)
                if fr.user == request.user:
                    fr.save()
                    return HttpResponseRedirect('../../')
                else:
                    error_text = "You do not have permission to edit this record"
            except ConcurrentModificationError as e:
                error_text = e;
        else:
            print (form.errors)
            error_text = form.errors
    else:
        feature_request = get_object_or_404(FeatureRequest, pk=feature_request_id)
        form = FeatureRequestForm(instance = feature_request)

    return render(request, 'feature_requests/edit.html',
    {
    'form': form,
    'feature_request_id' : feature_request_id,
    'client_list': Client.objects.all(),
    'product_area_list' : ProductArea.objects.all(),
    'error_text' : error_text
    })

#removes feature request
@login_required(login_url='/feature_requests/login/')
def delete(request, feature_request_id):
    fr = FeatureRequest.objects.get(pk=feature_request_id)
    if fr.user == request.user:
        fr.delete()
    return HttpResponseRedirect('../../')

#posts test data as requested by the app specifications to the DB if it does not exist
@login_required(login_url='/feature_requests/login/')
def addTestData(request):
    for letter in ('A', 'B', 'C'):
        if not Client.objects.filter(name = "Client " + letter).exists():
            client = Client(name = "Client " + letter)
            client.save()
    for product_name in ('Policies', 'Billing', 'Claims', 'Reports'):
        if not ProductArea.objects.filter(product_category = product_name).exists():
            pa = ProductArea(product_category = product_name)
            pa.save()
    return HttpResponseRedirect('../')
