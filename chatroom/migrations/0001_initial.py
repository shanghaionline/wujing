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
            name='ChatUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, help_text='', verbose_name='ID')),
                ('name', models.CharField(help_text='', max_length=100)),
                ('user_type', models.IntegerField(default=0, help_text='', choices=[(0, b'\xe6\x9c\xaa\xe7\x9f\xa5'), (1, b'\xe7\x94\xa8\xe6\x88\xb7'), (2, b'\xe9\xa2\x91\xe9\x81\x93')])),
                ('created', models.DateTimeField(help_text='')),
                ('last_access', models.DateTimeField(help_text='')),
                ('user', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, help_text='', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dialogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, help_text='', verbose_name='ID')),
                ('right', models.CharField(help_text='', max_length=80)),
                ('last_access', models.DateTimeField(help_text='')),
                ('owner', models.ForeignKey(help_text='', to='chatroom.ChatUser')),
                ('target', models.ForeignKey(related_name='+', to='chatroom.ChatUser', help_text='', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, help_text='', verbose_name='ID')),
                ('message', models.TextField(help_text='')),
                ('created', models.DateTimeField(help_text='')),
                ('source', models.ForeignKey(related_name='+', to='chatroom.ChatUser', help_text='')),
                ('target', models.ForeignKey(help_text='', to='chatroom.ChatUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
