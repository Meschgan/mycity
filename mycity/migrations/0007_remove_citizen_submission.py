# Generated by Django 4.0.6 on 2022-07-31 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0006_remove_citizen_level_remove_citizen_lft_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizen',
            name='submission',
        ),
    ]