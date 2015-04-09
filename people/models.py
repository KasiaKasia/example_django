from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):

    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=255, )
    last_name = models.CharField(max_length=255, )
    website = models.URLField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return ' '.join([
            self.first_name,
            self.last_name,
        ])

    def get_absolute_url(self):
        return reverse('people-view', kwargs={'pk': self.id})


class Project(models.Model):
    # dołączenie atrybutów odpowiadających kolumnom w tabeli
    person = models.ForeignKey(Person)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

