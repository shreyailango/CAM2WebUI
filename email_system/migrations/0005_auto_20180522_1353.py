# Generated by Django 2.0.5 on 2018-05-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_system', '0004_contactmodel_joinmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='joinmodel',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
