from django.db import models

# Create your models here.

class jobs(models.Model):
    image=models.ImageField(upload_to="images/")
    company_name=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    body=models.TextField()
    link=models.CharField(max_length=100)