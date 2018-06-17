# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class User (models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=100, blank=True, default='')
    lastname = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=50, blank=True, default='')


    class Meta:
        ordering = ('created',)