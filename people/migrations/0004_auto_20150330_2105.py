# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20150329_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='person',
            field=models.ManyToManyField(to='people.Person'),
            preserve_default=True,
        ),
    ]
