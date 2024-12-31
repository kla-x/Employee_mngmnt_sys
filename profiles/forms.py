from django import forms
from accounts.models import User

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone_number', 'profile_picture']
        widgets = {
            'profile_picture': forms.FileInput(),
        }