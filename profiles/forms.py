# forms.py
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'name', 'email', 'phone_no', 'country', 'city']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': field.replace('_', ' ').capitalize()})
            self.fields[field].label = ''

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        if not phone_no.isdigit():
            raise forms.ValidationError(
                'Phone number must contain only numeric characters.')
        return phone_no
