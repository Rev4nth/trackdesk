# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=40)),
                ('user_role', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='tickets',
            name='ticket_creator',
            field=models.ForeignKey(default='admin', on_delete=django.db.models.deletion.CASCADE, to='tracking.Users'),
        ),
    ]
