__author__ = 'KatarzynaAleksandra'
from django import forms
from people.models import Person, Project


class PersonForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

    # Klasa do obsługi metadanych związanym z forms
    class Meta:
        model = Person


class ProjectForm(forms.ModelForm):

    name = forms.CharField(max_length=128 )

    class Meta:
        model = Project
        fields = ('name',)