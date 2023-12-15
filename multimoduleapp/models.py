from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    usertype= models.CharField(default=1,max_length=10)
    
class Usermember(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    age=models.IntegerField()
    number=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to="images/",null=True)
