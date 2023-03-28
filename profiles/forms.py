from django import forms
from .models import Profile

class ProfileCreateForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "username"}))
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['created_at', 'updated_at']
    
    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        if ' ' in username:
            raise forms.ValidationError("This is not a valid username")
        return username


class RawProfileForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "username"}))
    name = forms.CharField(widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "your name",
                                        "rows": 20,
                                        "cols": 120
                                    }
                                )
                            )
    
