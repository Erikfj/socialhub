# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HubNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField()),
                ('points', models.PositiveIntegerField(default=0)),
                ('created_datetime', models.DateTimeField()),
                ('created_by', models.ForeignKey(related_name='created_notes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='notes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
