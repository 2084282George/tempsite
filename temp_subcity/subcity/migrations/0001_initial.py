# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2020-01-25 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('date', models.DateField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subcity.Show'),
        ),
    ]