# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gamestore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usertypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usertype', models.BooleanField(default=1)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='games',
            name='developer',
        ),
        migrations.DeleteModel(
            name='Games',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
