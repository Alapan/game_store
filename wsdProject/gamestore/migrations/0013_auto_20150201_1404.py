# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0012_scores'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scores',
            old_name='highest_score',
            new_name='high_score_1',
        ),
        migrations.RenameField(
            model_name='scores',
            old_name='most_recent_score',
            new_name='high_score_2',
        ),
        migrations.AddField(
            model_name='scores',
            name='gamestate',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scores',
            name='high_score_3',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scores',
            name='high_score_4',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scores',
            name='high_score_5',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scores',
            name='last_score',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
