from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from .models import Person

class PersonForm(forms.ModelForm):
    name    = forms.CharField(
                    widget = forms.TextInput(
                        attrs={
                            'placeholder': 'Enter your name'})
                        )
    email = forms.EmailField(
                    widget = forms.EmailInput(
                        attrs={
                            'placeholder': 'Enter your email'})
                        )
    age     = forms.IntegerField(
                    widget = forms.TextInput(
                        attrs={
                            'placeholder': 'Enter your age'})
                        )
    bio     = forms.CharField(
                    required=False, widget=forms.Textarea(
                        attrs={'placeholder':'Enter a short description'})
                        )

    class Meta:
        model = Person
        fields = [
            'name',
            'email',
            'age',
            'bio'
        ]
    
    #Custom verification
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("gmail.com"):
            raise forms.ValidationError("Email must be from Google")
        return email

class RawPersonForm(forms.Form):
    name    = forms.CharField(
                    widget = forms.TextInput(
                        attrs={
                            'placeholder': 'Enter your name'
                        }
                    )
                )
    email = forms.EmailField(
                    widget = forms.TextInput(
                        attrs={
                            'placeholder': 'Enter your email'
                        }
                    )
                )
    age     = forms.IntegerField(
                    widget = forms.TextInput(
                        attrs={
                            'placeholder': 'Enter your age'
                        }
                    )
                )
    bio     = forms.CharField(
                    required=False, widget=forms.Textarea(
                        attrs={
                            'placeholder':'Enter a short description'
                        }
                    )
                )
