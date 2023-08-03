from django.db import models

# Create your models here.
class Intro(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    hometown=models.CharField(max_length=100)
    present_address=models.CharField(max_length=100)
    occupation=models.CharField(max_length=100)
    height=models.CharField(max_length=100)
    color=models.CharField(max_length=100)

    



