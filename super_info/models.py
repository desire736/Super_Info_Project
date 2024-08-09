from django.db import models

class Hashtags(models.Model):
   title = models.CharField(max_length=255)

class Category(models.Model):
   title = models.CharField(max_length=255)

class Publications(models.Model):

   category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='publication', null=True)
   hashtags = models.ManyToManyField(Hashtags, related_name='publication')
   title = models.CharField(max_length=255)
   short_description = models.TextField(null=True)
   description = models.TextField()
   datetime = models.DateField()
   is_active = models.BooleanField(default=True)

