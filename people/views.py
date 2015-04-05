from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from people.forms import PersonForm, ProjectForm
from people.models import Person, Project
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

def index(request):
    context = RequestContext(request)

    person_list = Person.objects.order_by('-first_name')[:15]
    context_dict = {'people-list': person_list}
    return render_to_response('list_person.html', context_dict, context)



def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Person.objects.filter(id=starts_with)
    else:
        cat_list = Person.objects.all()

    if max_results > 0:
        if (len(cat_list) > max_results):
            cat_list = cat_list[:max_results]

    for cat in cat_list:
        cat.first_name = cat.first_name
        cat.last_name = cat.last_name
        cat.email = cat.email

def person_(request, person_id_name):

    context = RequestContext(request)
    person_id = person_id_name.replace('_', ' ')
    context_dict = {'person_id': person_id}

    try:
        people = Person.objects.get(id=person_id)

        projects = Project.objects.filter(person=people)
        context_dict['projects'] = projects
        context_dict['people'] = people
    except Person.DoesNotExist:
        pass

    return render_to_response('add_project.html', context_dict, context)

def add_project(request, person_id_name):
    context = RequestContext(request)
    cat_list = get_category_list()
    context_dict = {}
    context_dict['cat_list'] = cat_list

    person = person_id_name
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)

            try:
                cat = Person.objects.get(id=person)
                project.person = cat
            except Person.DoesNotExist:
                return render_to_response('add_project.html',
                    {}, context)

            project.views = 0

            project.save()
            return person_(request, person_id_name)
        else:
            print(form.errors)
    else:
        form = ProjectForm()

    context_dict['person_id_name']= person_id_name
    context_dict['person_id'] =  person
    context_dict['form'] = form

    return render_to_response( 'add_project.html',
                               context_dict, context)