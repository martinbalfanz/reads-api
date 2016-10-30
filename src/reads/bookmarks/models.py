from django.db import models


class Bookmark(models.Model):
    href = models.URLField(max_length=400)
    description = models.TextField()
    extended = models.TextField()
    meta = models.CharField(max_length=32, unique=True)
    hash = models.CharField(max_length=32, unique=True)
    time = models.DateTimeField(auto_now_add=True)
    shared = models.BooleanField()
    toread = models.BooleanField()
    tags = models.TextField(blank=True)
