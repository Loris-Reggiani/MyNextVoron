# Generated by Django 4.2.3 on 2023-10-11 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_credentials_mission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='first_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='auth',
            name='last_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
