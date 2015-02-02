# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0015_auto_20150202_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='last_score',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
