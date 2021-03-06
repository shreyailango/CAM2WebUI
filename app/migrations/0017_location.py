# Generated by Django 2.0.5 on 2018-06-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20180627_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officename', models.CharField(max_length=100, verbose_name='Office Name')),
                ('officeroom', models.CharField(blank=True, max_length=50, null=True, verbose_name='Room Number')),
                ('officebldg', models.CharField(blank=True, max_length=100, null=True, verbose_name='Building')),
                ('officeaddr', models.CharField(max_length=100, verbose_name='Address')),
                ('officecity', models.CharField(max_length=100, verbose_name='City')),
                ('officestate', models.CharField(max_length=2, verbose_name='State')),
                ('officezip', models.CharField(max_length=50, verbose_name='Zip Code')),
                ('officenum', models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone Number')),
            ],
        ),
    ]
