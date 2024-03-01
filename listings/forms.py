# forms.py
from .models import Service
from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_type', 'transaction_type', 'bhk', 'address',
                  'picture1', 'picture2', 'picture3', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
   
        for field_name in ['property_type', 'transaction_type', 'bhk', 'address', 'picture1', 'picture2', 'picture3', 'description', 'price']:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            self.fields[field_name].widget.attrs['placeholder'] = field_name.replace('_', ' ').capitalize()
            self.fields[field_name].label = ''


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'country', 'city', 'available_location', 'google_profile']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields_to_customize = ['title', 'country', 'city', 'available_location', 'google_profile']
        for field_name in fields_to_customize:
            self.fields[field_name].widget.attrs.update({'class': 'form-control', 'placeholder': field_name.replace('_', ' ').capitalize()})
            self.fields[field_name].label = ''
