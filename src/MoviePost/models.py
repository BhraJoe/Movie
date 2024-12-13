from django.db import models

# Create your models here.

class MoviePost(models.Model):
    objects = None
    name = models.CharField(max_length=255,null=True)
    image = models.ImageField(null=True,blank=True,upload_to='images/')
    # video = models.FileField(null=True,blank=True,upload_to='videos/')
    description = models.TextField(null=True,max_length=255)
    videolink = models.TextField(null=True,max_length=255)
    




    def __str__(self):
        return self.name


#
# class Score(models.Model):
#     name = models.CharField('Venue Name',max_length=255,null=True)
#     email_address = models.EmailField('Email Address', blank=True)
#     comments = models.TextField('Comments',null=True,max_length=255)
#
#
#     def __str__(self):
#         return self.name
