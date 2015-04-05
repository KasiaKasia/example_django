# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20150330_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='person',
        ),
    ]
