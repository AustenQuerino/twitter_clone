from django import forms
from .models import Profile

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['created_at', 'updated_at']

class RawProfileForm(forms.Form):
    username = forms.CharField()
    name = forms.CharField()
    