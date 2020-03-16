from django.db import models

# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=100)
    sub_title=models.CharField(max_length=200)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")