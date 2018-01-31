from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

import os.path

class Recordings(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='recordings',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=1,
        )
    device = models.CharField(max_length=30, blank=False, default='unknown')
    datafile = models.FileField(upload_to='uploads/%Y/%m/%d/')
    result = models.CharField(max_length=200, blank=True, default='()')

    class Meta:
        ordering=('owner','-created')
        # ordering=('-created',)

class UserInfo(models.Model):
    owner = models.ForeignKey(
        'auth.User',
        related_name='userinfo',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=1,
        )
    gender = models.CharField(max_length=7, blank=False, default='unknown')
    age = models.CharField(max_length=7, blank=False, default='unknown')

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
