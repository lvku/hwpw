# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PreRegisterPhone(models.Model):
    STATUS_CHOICES = (
        ('NEW', 'NEW'),
        ('SENT', 'SENT'),
        ('DONE', 'DONE'),
    )
    phone_text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='NEW')
