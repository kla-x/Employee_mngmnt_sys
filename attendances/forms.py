from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['status']
        widgets = {
            'status': forms.RadioSelect(choices=[(True, 'Present'), (False, 'Absent')])
        }