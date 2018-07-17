# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_merge_20170612_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentmember',
            name='currentmemberimg',
            field=models.CharField(max_length=300, verbose_name='Current Member Image'),
        ),
        migrations.AlterField(
            model_name='currentmember',
            name='currentmembername',
            field=models.CharField(max_length=50, verbose_name='Current Member Name'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.CharField(max_length=500, verbose_name='FAQ answer'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=200, verbose_name='FAQ question'),
        ),
        migrations.AlterField(
            model_name='history',
            name='event',
            field=models.CharField(max_length=500, verbose_name='History Details'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='leaderimg',
            field=models.CharField(max_length=300, verbose_name='Leader Image'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='leadername',
            field=models.CharField(max_length=50, verbose_name='Leader Name'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='leaderpagelink',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Leader Page Link (Optional)'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='leadertitle',
            field=models.CharField(max_length=50, verbose_name='Leader Title'),
        ),
        migrations.AlterField(
            model_name='oldmember',
            name='oldmembername',
            field=models.CharField(max_length=50, verbose_name='Old Member Name'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='paperinfo',
            field=models.CharField(max_length=500, verbose_name='Publication Details'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='paperlink',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Publication Paper Link (Optional)'),
        ),
        migrations.AlterField(
            model_name='team',
            name='teamimg',
            field=models.CharField(max_length=300, verbose_name='Team Image'),
        ),
    ]
