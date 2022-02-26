from operator import mod
from django.db import models

# Create your models here.


class ContactModel(models.Model):

    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    address = models.TextField()

    
    def __str__(self):
        return self.name






