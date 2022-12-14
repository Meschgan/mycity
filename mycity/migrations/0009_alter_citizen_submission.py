# Generated by Django 4.0.6 on 2022-07-31 10:20

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0008_citizen_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='submission',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='citizen', to='mycity.citizen'),
        ),
    ]
