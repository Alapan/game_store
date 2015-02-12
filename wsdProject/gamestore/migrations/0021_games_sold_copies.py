# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0020_games_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='sold_copies',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
