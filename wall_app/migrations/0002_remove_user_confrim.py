# Generated by Django 2.2 on 2020-02-18 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confrim',
        ),
    ]
