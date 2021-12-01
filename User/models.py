from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):  
    # user = models.OneToOneField(User,on_delete=models.CASCADE,default='')
    # USERNAME_FIELD = 'username'
    #other fields here
    name = models.CharField(max_length=200,default='')
    address = models.CharField(max_length=200,default='')
    accountnumber = models.CharField(max_length=200,default='')
    username = models.CharField(max_length=200,default='')

    def __str__(self):  
          return  self.name  

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 

#in settings.py
AUTH_PROFILE_MODULE = 'User.UserProfile'