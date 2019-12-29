from django.db import models
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length = 256)
    description = models.TextField()
    price = models.FloatField()
    image = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item:detail', kwargs={'pk':self.pk})

