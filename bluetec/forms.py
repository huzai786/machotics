from django import forms
from .models import GetStarted


class GetStartedForm(forms.ModelForm):
    class Meta:
        model = GetStarted
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'size': 5, 'class': 'form-control', 'placeholder': 'Enter your name:'})
        self.fields['phone_no'].widget.attrs.update({'size': 5, 'title': 'Phone No', 'class': 'form-control', 'placeholder': 'Enter your phone no(Optional):'})
        self.fields['email'].widget.attrs.update({'size': 10, 'title': 'Email', 'class': 'form-control', 'placeholder': 'Enter your email:'})
        self.fields['description'].widget.attrs.update({'size': 10, 'title': 'description', 'class': 'form-control', 'placeholder': 'Enter your projects description:'})

