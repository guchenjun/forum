# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    coin = models.IntegerField(default=0)
    deposit = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)
    replies = models.IntegerField(default=0)
    mod_date = models.DateTimeField('Last modified', auto_now=True)

    class Meta:
        verbose_name = 'User Profile'

    def __str__(self):
        return self.user.__str__()
