# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class contact(models.Model):
    username = models.ForeignKey(User)
    mobileno = models.CharField(max_length=50)

class messcanteen(models.Model):
    incharge = models.ForeignKey(User,related_name='owner')
    messcanteen = models.CharField(max_length=50)
    def __str__(self):
        return self.messcanteen 

class diet(models.Model):
    messname = models.ForeignKey(messcanteen)
    customer = models.ForeignKey(User)
    remarks = models.CharField(max_length=200)
    amount = models.IntegerField(default = 0)
    verified = models.BooleanField(default=False)
    ts = models.DateTimeField(auto_now_add=True)

class credittable(models.Model):
    messname = models.ForeignKey(messcanteen)
    customer = models.ForeignKey(User)
    credit = models.IntegerField(default = 0)



class urlshort(models.Model):
    dietplan = models.ForeignKey(diet)
    link = models.CharField(max_length=200)

    