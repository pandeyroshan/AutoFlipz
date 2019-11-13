from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='My Name')
    image= models.ImageField(default = 'default.jpg', upload_to='profile_pic')
    phoneNumber = models.CharField(max_length=15,blank=True)
    addressL1 = models.CharField(max_length=300,blank=True)
    addressL2 = models.CharField(max_length=200,blank=True)
    addressL3 = models.CharField(max_length=100,blank=True)
    coins = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username+' Profile'
    
    class Meta:
        verbose_name= 'User Profiles'
        verbose_name_plural = 'User Profiles'