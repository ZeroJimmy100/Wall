# Generated by Django 2.2 on 2020-02-19 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0003_auto_20200218_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='users',
        ),
        migrations.AddField(
            model_name='comment',
            name='users',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='ItUser', to='wall_app.User'),
            preserve_default=False,
        ),
    ]