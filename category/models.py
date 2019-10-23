from django.db import models

# Create your models here.
from django.utils import timezone


class Category1(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    status = models.IntegerField(default=1, blank=True)
    ctime = models.DateTimeField(default=timezone.now)
    mtime = models.DateTimeField(auto_now=True)

class Category2(models.Model):
    id = models.AutoField(primary_key=True)
    father_id = models.IntegerField()
    name = models.CharField(max_length=100,unique=True)
    status = models.IntegerField(default=1, blank=True)
    ctime = models.DateTimeField(default=timezone.now)
    mtime = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('father_id', 'name')