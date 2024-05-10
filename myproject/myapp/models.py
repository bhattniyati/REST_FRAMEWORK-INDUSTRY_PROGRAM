from django.db import models
from django.utils import timezone
# Create your models here.

# create a class name of Comment 
class Comment(models.Model):
    text= models.TextField()
    author=models.CharField(max_length=30)
    created_at=models.DateTimeField(default = timezone.now)
    
    # this method show in admin panel 
    def __str__(self):
        return self.author