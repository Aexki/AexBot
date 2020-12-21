from django.db import models

# Create your models here.
class Message(models.Model):
    name=models.CharField(max_length=50)
    message=models.CharField(max_length=100)
    type=models.CharField(max_length=20)
    sendtime=models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

