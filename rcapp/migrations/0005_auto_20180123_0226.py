# Generated by Django 2.0.1 on 2018-01-22 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rcapp', '0004_auto_20180123_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordings',
            name='owner',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recordings', to=settings.AUTH_USER_MODEL),
        ),
    ]
