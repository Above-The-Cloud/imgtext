from django.db import models

# Create your models here.
from django.utils import timezone


class Article(models.Model):
    cover = models.CharField(max_length=200)
    desc = models.TextField()
    text = models.TextField()
    source = models.IntegerField()
    org_id = models.IntegerField(default=0, blank=True)
    link = models.CharField(max_length=200)
    author = models.CharField(max_length=200,blank=True, null=True)
    category1 = models.IntegerField(blank=True, null=True)
    category2 = models.IntegerField(blank=True, null=True)
    rstatus = models.IntegerField(default=1, blank=True)
    meta1 = models.IntegerField(blank=True, null=True)
    meta2 = models.CharField(max_length=200,blank=True, null=True)
    meta3 = models.CharField(max_length=400,blank=True, null=True)
    status = models.IntegerField(default=1, blank=True)
    ctime = models.DateTimeField(default = timezone.now)
    mtime = models.DateTimeField(auto_now = True)

    class Meta:
        unique_together = ('source', 'org_id')