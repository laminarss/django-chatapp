from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserToken(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  token = models.CharField(max_length=255)
  status = models.BooleanField()
  
  def set_user_token(self, user, token, status=False):
    self.user = user
    self.token = token
    self.status = status
    
class ChatRoom(models.Model):
  id = models.BigAutoField(primary_key=True)
  room = models.CharField(max_length=255)
    
class Messsages(models.Model):
  id = models.BigAutoField(primary_key=True)
  message = models.CharField(max_length=255)
  room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)