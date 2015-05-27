# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hubs', '0003_auto_20150522_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hubnote',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='hub',
            name='username',
            field=models.ForeignKey(related_name='notes', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hubnote',
            name='user',
            field=models.ForeignKey(related_name='notes_2', to=settings.AUTH_USER_MODEL),
        ),
    ]
