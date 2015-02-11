# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0016_auto_20150202_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertypes',
            name='developer',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
