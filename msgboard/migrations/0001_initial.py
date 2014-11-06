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
            name='BoardMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('tag', models.CharField(max_length=200)),
                ('agreeTimes', models.IntegerField(default=0)),
                ('created', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'verbose_name_plural': '留言',
                'verbose_name': '留言',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MsgTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('text', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': '标签',
                'verbose_name': '标签',
            },
            bases=(models.Model,),
        ),
    ]
