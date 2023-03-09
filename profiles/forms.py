
from django import forms
from .models import Profile

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'username',
            'name',
            'bio', 
        ]

