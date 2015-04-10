__author__ = 'KatarzynaAleksandra'
from django import forms
from people.models import Person, Project
from django.contrib.auth.models import User

class PersonForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    website = forms.URLField()

    # Klasa do obsługi metadanych związanym z forms
    class Meta:
        model = Person


class ProjectForm(forms.ModelForm):

    name = forms.CharField(max_length=128 )

    class Meta:
        model = Project
        fields = ('name',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User

        fields = ('username','email',  'password')
