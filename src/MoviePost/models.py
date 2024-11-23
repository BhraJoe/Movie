from django.db import models

# Create your models here.

class MoviePost(models.Model):
    name = models.CharField(max_length=255,null=True)
    image = models.ImageField(null=True,blank=True,upload_to='images/')
    # video = models.FileField(null=True,blank=True,upload_to='vidoes/')
    # description = models.TextField(max_length=255)




    def __str__(self):
        return self.name