# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0018_remove_usertypes_developer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertypes',
            name='usertype',
        ),
        migrations.AddField(
            model_name='usertypes',
            name='developer',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
