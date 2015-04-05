# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_remove_project_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='person_id',
            field=models.ForeignKey(default=1, to='people.Person'),
            preserve_default=False,
        ),
    ]
