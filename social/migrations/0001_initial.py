# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 15:35
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Following'), (2, 'Blocked')])),
                ('rel_date', models.DateTimeField(verbose_name=datetime.datetime(2017, 9, 30, 17, 35, 56, 498841))),
                ('from_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_people', to='social.Profile')),
                ('to_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_people', to='social.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='relationships',
            field=models.ManyToManyField(related_name='related_to', through='social.Relationship', to='social.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
