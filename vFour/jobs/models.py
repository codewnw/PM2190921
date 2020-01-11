from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    experience = models.IntegerField(default=0)
    location = models.CharField(default = 'Bangalore', max_length=256)
