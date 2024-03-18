from django.db import models

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    