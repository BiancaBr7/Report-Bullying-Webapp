from django import forms
from django.core.validators import EmailValidator
from django import forms
from .models import Form


class Form(forms.ModelForm):
    class Meta:
        model = Form  # Replace YourModel with your actual model class
        fields = ['name', 'email', 'school_name', 'school_email', 'category', 'language','message']
        labels = {
            'name': 'Name',
            'email':'Email',
            'school_name': 'School Name',
            'school_email': 'School Email',
            'category': 'Form of Bullying',
            'language': "Language You Choose to Describe",
            'message': 'Description of the Situation'
        }