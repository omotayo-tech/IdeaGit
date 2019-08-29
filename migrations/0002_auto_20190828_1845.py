# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-28 23:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('composer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='News.User')),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_of_view', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added', models.BooleanField(default=False)),
                ('added_at', models.DateTimeField(blank=True, null=True)),
                ('likes', models.ManyToManyField(related_name='liked_by', to='News.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thoughts', to='News.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='my_opinion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='News.Opinion'),
        ),
    ]
