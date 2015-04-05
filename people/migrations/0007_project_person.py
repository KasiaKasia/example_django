# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_remove_project_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='person',
            field=models.ForeignKey(to='people.Person', default=1),
            preserve_default=False,
        ),
    ]
