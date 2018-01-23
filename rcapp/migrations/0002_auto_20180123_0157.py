# Generated by Django 2.0.1 on 2018-01-22 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rcapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recordings',
            options={'ordering': ('owner', '-created')},
        ),
        migrations.AddField(
            model_name='recordings',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='recordings', to=settings.AUTH_USER_MODEL),
        ),
    ]
