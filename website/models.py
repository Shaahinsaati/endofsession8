from re import T
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=250,null=True,blank=True)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s - %s'%(self.id, self.name)


class Newsletter(models.Model):
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.email