from django.db import models

# Create your models here.

class MoviePost(models.Model):
    name = models.CharField(max_length=255,null=True)




    def __str__(self):
        return str(self)