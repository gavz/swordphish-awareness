# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-03-30 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_anonymoustarget_mail_sent_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campaign',
            options={'ordering': ['-start_date', '-end_date', 'creation_date']},
        ),
        migrations.AlterModelOptions(
            name='phishmaildomain',
            options={'ordering': ['domain']},
        ),
        migrations.AlterModelOptions(
            name='targetlist',
            options={'ordering': ['name', '-creation_date']},
        ),
        migrations.AlterModelOptions(
            name='template',
            options={'ordering': ['name', '-creation_date']},
        ),
        migrations.AlterField(
            model_name='attribute',
            name='key',
            field=models.CharField(db_index=True, max_length=240),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='value',
            field=models.CharField(db_index=True, max_length=240),
        ),
        migrations.AlterField(
            model_name='target',
            name='mail_address',
            field=models.EmailField(db_index=True, max_length=254),
        ),
    ]