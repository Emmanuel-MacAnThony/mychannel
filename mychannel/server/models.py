from typing import Iterable
from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name

class Server(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="server_owner")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="server_category")
    description = models.CharField(blank=True, null=True, max_length=500)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL)
    
    def __str__(self) -> str:
        return self.name
    
class Channel(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="channel_owner")
    topic = models.CharField(max_length=100)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="channel_server")
    
    def __str__(self) -> str:
        return self.name
        
    
    def save(self, *args, **kwargs) -> None:
        self.name = self.name.lower()
        super(Channel, self).save(*args, **kwargs)