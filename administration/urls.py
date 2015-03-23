from django.conf.urls import patterns, include, url
from django.contrib import admin
import people.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'administration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', people.views.ListPersonView.as_view(),
        name='people-list',),
    url(r'^new$', people.views.CreatePersonView.as_view(),
        name='person-new',),
    url(r'^edit/(?P<pk>\d+)/$', people.views.UpdatePersonView.as_view(),
        name='people-edit',),
    url(r'^delete/(?P<pk>\d+)/$', people.views.DeletePersonView.as_view(),
        name='person-delete',),
    url(r'^(?P<pk>\d+)/$', people.views.PersonView.as_view(),
        name='people-view',),

)
urlpatterns += staticfiles_urlpatterns()