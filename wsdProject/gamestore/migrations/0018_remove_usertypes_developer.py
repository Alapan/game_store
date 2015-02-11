# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0017_usertypes_developer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertypes',
            name='developer',
        ),
    ]
