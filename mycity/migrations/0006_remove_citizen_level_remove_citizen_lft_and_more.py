# Generated by Django 4.0.6 on 2022-07-31 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0005_rename_submission_citizen_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizen',
            name='level',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='tree_id',
        ),
        migrations.AddField(
            model_name='citizen',
            name='submission',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='citizen', to='mycity.citizen'),
        ),
    ]
