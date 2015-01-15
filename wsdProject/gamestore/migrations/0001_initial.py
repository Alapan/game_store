# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('url', models.URLField()),
                ('price', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(unique=True, max_length=100)),
                ('last_name', models.CharField(unique=True, max_length=100)),
                ('user_name', models.CharField(unique=True, max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(unique=True, max_length=70)),
                ('type', models.BooleanField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='games',
            name='developer',
            field=models.OneToOneField(to='gamestore.Users'),
            preserve_default=True,
        ),
    ]
