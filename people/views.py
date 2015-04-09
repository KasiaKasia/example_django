from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import is_password_usable
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView,\
    DetailView,\
    CreateView,\
    UpdateView,\
    DeleteView
from people.forms import PersonForm, ProjectForm, UserForm
from people.models import Person, Project
from django.core.urlresolvers import reverse


# Tworzenie widoków
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
    list = []
    if starts_with:
        list = Person.objects.filter(id=starts_with)
    else:
        list = Person.objects.all()

    if max_results > 0:
        if (len(list) > max_results):
            list = list[:max_results]

<<<<<<< HEAD
=======

    return list
>>>>>>> origin/master

    return list

def person_(request, person_id_name):
    # pobranie żądania
    context = RequestContext(request)
    person_id = person_id_name
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
    list = get_category_list()
    context_dict = {}
    context_dict['list'] = list

    person = person_id_name
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)

            try:
                x = Person.objects.get(id=person)
                project.person = x
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


def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")

def register(request):

    context = RequestContext(request)

    list = get_category_list()
    context_dict = {}
    context_dict['list'] = list

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)

            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print (user_form.errors)
    else:
        user_form = UserForm()

    return render_to_response(
            'register.html',
            {'user_form': user_form,
             'registered': registered},
            context)

def user_login(request):
    context = RequestContext(request)

    list = get_category_list()
    context_dict = {}
    context_dict['list'] = list

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        '''
         Uwierzytelnianie użytkowników - właczenie w settings :
         'django.contrib.auth'
         'django.contrib.contenttypes'
        '''
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return  HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('login.html', {}, context)


#@login_required - dekorator
@login_required
def restricted(request):
    context = RequestContext(request)

    list = get_category_list()
    context_dict = {}
    context_dict['list'] = list
    return render_to_response('restricted.html', context_dict, context)

@login_required
def user_logout(request):

    logout(request)

    return HttpResponseRedirect('/')
