# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_no=models.CharField(max_length=6,primary_key=True)
    birth_date=models.DateField(auto_now=False, auto_now_add=False)
    first_name=models.CharField(max_length=14)
    last_name=models.CharField(max_length=16)
    gender=models.CharField(max_length=1)
    hire_date=models.DateField(auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return self.emp_no

