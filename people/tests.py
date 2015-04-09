from django.test import TestCase

# Tworzenie testów
from people.models import Person

class PersonTests(TestCase):
    """Contact model tests."""

    def test_str(self):

        person = Person(first_name='Name', last_name='last name')

        self.assertEquals(str(person),
            'Name last name',
            )