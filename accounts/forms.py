

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Department, Role







class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone_number = forms.CharField(max_length=20)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    role = forms.ModelChoiceField(queryset=Role.objects.all())
    bank_account_number = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 
                  'password1', 'password2',  'phone_number',
                    'department', 'role', 'bank_account_number']