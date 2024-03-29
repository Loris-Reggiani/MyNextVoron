# Generated by Django 4.2.3 on 2023-10-11 10:13

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_merge_20230920_1948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mission',
            options={'ordering': ['start', 'id'], 'verbose_name': 'Mission', 'verbose_name_plural': 'Missions'},
        ),
        migrations.AddField(
            model_name='reporthtml',
            name='html_file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='reporthtml',
            name='logo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mission',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='missions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mission',
            name='last_updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_updated_missions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mission',
            name='recon',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mission', to='api.recon'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_of', to='api.team'),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), blank=True, null=True, size=4),
        ),
    ]
