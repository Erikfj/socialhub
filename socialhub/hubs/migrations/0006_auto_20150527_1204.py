# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hubs', '0005_auto_20150527_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='hub',
            name='created_by',
            field=models.ForeignKey(related_name='created_notes', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hub',
            name='created_datetime',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hubnote',
            name='created_by',
            field=models.ForeignKey(related_name='created_notes_2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hubnote',
            name='created_datetime',
            field=models.TextField(),
        ),
    ]
