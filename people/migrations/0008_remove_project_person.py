# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_project_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='person',
        ),
    ]
