from django.db import models

# Create your models here.


class enquiry(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()

class gallery(models.Model):
    image = models.ImageField()

class blogs(models.Model):
    title = models.CharField(max_length=15)
    image = models.ImageField()
    description = models.TextField()

class registeruser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

class login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)

