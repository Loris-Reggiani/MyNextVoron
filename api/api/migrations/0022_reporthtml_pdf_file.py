# Generated by Django 4.2.3 on 2023-11-17 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_merge_20231011_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporthtml',
            name='pdf_file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
