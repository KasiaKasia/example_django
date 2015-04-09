from django.contrib import admin
from people.models import Person, Project


'''
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Person)
admin.site.register(Project, ProjectAdmin)
'''