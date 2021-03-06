# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 07:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('functions', '0005_taskslist'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followUserID', models.CharField(max_length=30)),
                ('Time', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('AppName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='functions.TwitterApp')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetID', models.CharField(max_length=30)),
                ('Time', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('AppName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='functions.TwitterApp')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskreTweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetID', models.CharField(max_length=30)),
                ('Time', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('AppName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='functions.TwitterApp')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
