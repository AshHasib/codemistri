from django.db import models

# Create your models here.

class Contestant(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length = 128)
    username = models.CharField(max_length = 20)
    email = models.EmailField()
    profile_img = models.ImageField(upload_to = 'img/profile_pic')
    passwd = models.CharField(max_length = 20)
    rank = models.CharField(max_length = 10, default= 'NOOB')
    score = models.IntegerField(default = 0)


    def __str__(self):
        return self.username

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length = 128)
    username = models.CharField(max_length = 20)
    email = models.EmailField()
    profile_img = models.ImageField(upload_to = 'img/admin_profile_pic')
    passwd = models.CharField(max_length = 20)

    def __str__(self):
        return self.username