# Generated by Django 4.0.5 on 2022-07-31 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='information',
            name='password',
        ),
        migrations.RemoveField(
            model_name='information',
            name='username',
        ),
        migrations.RemoveField(
            model_name='information',
            name='wcode',
        ),
    ]
