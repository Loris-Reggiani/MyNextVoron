# Generated by Django 4.2.3 on 2023-09-12 18:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_nmapscan_nmap_version_nmapscan_os_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='scope',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, max_length=64, null=True, size=None),
        ),
    ]
