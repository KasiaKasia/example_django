from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Person(models.Model):

    first_name = models.CharField(max_length=255,)
    last_name = models.CharField(max_length=255,)
    email = models.EmailField()

    def __str__(self):

        return ' '.join([
            self.first_name,
            self.last_name,
        ])

    def get_absolute_url(self):

        return reverse('people-view', kwargs={'pk': self.id})