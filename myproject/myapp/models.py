from django.db import models
from django.utils import timezone
# Create your models here.

# create a class name of Comment 
class Comment(models.Model):
    title= models.CharField(max_length=30)
    code= models.CharField(max_length=50)
    linenos= models.BooleanField(default=False)
    language= models.CharField(max_length=20)
    style= models.CharField(max_length=20)
    
    # this method show in admin panel 
    def __str__(self):
        return self.title
