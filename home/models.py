from django.db import models

# Create your models here.


class Follower(models.Model):
    name = models.CharField(null = True , max_length=50) 
    email = models.EmailField(null = True  ) 
    phone_number = models.IntegerField(null = True ) 
    message = models.TextField( null = True ) 

    def __str__(self): 
        return self.name 
    
      