from django import forms
from .models import ApplicationInfo

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationInfo
        fields = ('first_name', 'last_name', 'qualification', 'email', 'mobile', 'others')
