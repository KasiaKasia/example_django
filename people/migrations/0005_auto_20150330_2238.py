# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20150330_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='person',
            field=models.ForeignKey(to='people.Person'),
            preserve_default=True,
        ),
    ]
