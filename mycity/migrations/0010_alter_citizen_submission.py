# Generated by Django 4.0.6 on 2022-07-31 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0009_alter_citizen_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='submission',
            field=models.ForeignKey(blank=True, limit_choices_to={'self': 'self'}, on_delete=django.db.models.deletion.PROTECT, related_name='citizen', to='mycity.citizen'),
        ),
    ]
