# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0013_auto_20150201_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='high_score_1',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
