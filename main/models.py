from django.db import models

# Create your models here.



class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length = 128)
    username = models.CharField(max_length = 40)
    email = models.EmailField()
    profile_img = models.ImageField(upload_to = 'img/profile_pic')
    password = models.CharField(max_length = 20)
    user_type = models.CharField(max_length = 20)
    rank = models.CharField(max_length = 10, blank = True)
    score = models.IntegerField(default = 0)

    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields= ['username', 'user_type'], name = 'user_identity')
        ]
    
    def __str__(self):
        return self.username
