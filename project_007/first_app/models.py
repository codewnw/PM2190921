from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 255, unique = True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    name = models.CharField(max_length = 255, unique = True)

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    sub_category = models.ForeignKey(SubCategory, on_delete = models.PROTECT)
    name = models.CharField(max_length = 255, unique = True)
    description = models.CharField(max_length = 1024)
    image = models.CharField(max_length = 255)

    def __str__(self):
        return self.name + ', ' + self.description
