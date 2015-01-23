# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0004_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertypes',
            name='user',
        ),
        migrations.DeleteModel(
            name='Usertypes',
        ),
    ]
