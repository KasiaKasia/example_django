# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_project_person_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='person_id',
            new_name='person',
        ),
    ]
