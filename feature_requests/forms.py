from django.forms import ModelForm
from .models import FeatureRequest

class FeatureRequestForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'client', 'client_priority', 'target_date', 'ticket_url', 'product_area']
