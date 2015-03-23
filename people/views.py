from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from people.models import Person
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
class ListPersonView(ListView):

    model = Person
    template_name = 'list_person.html'

class CreatePersonView(CreateView):

    model = Person
    template_name = 'edit_person.html'

    def get_success_url(self):
        return reverse('people-list')
    def get_context_data(self, **kwargs):

        context = super(CreatePersonView, self).get_context_data(**kwargs)
        context['action'] = reverse('person-new')

        return context

class UpdatePersonView(UpdateView):

    model = Person
    template_name = 'edit_person.html'

    def get_success_url(self):
        return reverse('people-list')

    def get_context_data(self, **kwargs):

        context = super(UpdatePersonView, self).get_context_data(**kwargs)
        context['action'] = reverse('people-edit',
                                    kwargs={'pk': self.get_object().id})

        return context

class DeletePersonView(DeleteView):

    model = Person
    template_name = 'delete_person.html'

    def get_success_url(self):
        return reverse('people-list')

class PersonView(DetailView):

    model = Person
    template_name = 'person.html'