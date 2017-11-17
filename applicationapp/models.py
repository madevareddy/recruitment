from __future__ import unicode_literals

from django.db import models

class ApplicationInfo(models.Model):
     first_name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)
     qualification = models.CharField(max_length=30)
     email = models.CharField(max_length=30)
     mobile = models.IntegerField()
     others = models.CharField(max_length=300)
     status = models.CharField(max_length=30, default="")
