# Generated by Django 2.0.7 on 2018-07-12 18:57

import app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20180712_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='slidedescrb',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Slide Description'),
        ),
        migrations.AlterField(
            model_name='index',
            name='slideheader',
            field=models.CharField(blank=True, max_length=100, verbose_name='Slide Header'),
        ),
        migrations.AlterField(
            model_name='index',
            name='slidelink',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Image Link'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logolink',
            field=models.CharField(blank=True, max_length=300, null=True, validators=[app.validators.validateURL], verbose_name='Link to Logo'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='sponname',
            field=models.CharField(blank=True, max_length=100, verbose_name='Sponsor'),
        ),
    ]