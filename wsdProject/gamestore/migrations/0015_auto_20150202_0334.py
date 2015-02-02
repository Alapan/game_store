# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0014_auto_20150202_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='high_score_2',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scores',
            name='high_score_3',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scores',
            name='high_score_4',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scores',
            name='high_score_5',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
