# Generated by Django 3.0.2 on 2020-02-10 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200210_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='toys',
        ),
        migrations.DeleteModel(
            name='Toy',
        ),
    ]
