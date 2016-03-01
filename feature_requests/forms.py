from django.forms import ModelForm
from django import forms
from .models import FeatureRequest

class FeatureRequestForm(ModelForm):
    version = forms.IntegerField(required=False)
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'client', 'client_priority', 'target_date', 'ticket_url', 'product_area', 'version']

class FeatureRequestDescriptionForm(ModelForm):
    version = forms.IntegerField(required=False)
    class Meta:
        model = FeatureRequest
        fields = ['description', 'version']
