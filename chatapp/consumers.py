from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
  def connect(self):
    self.accept()
    
  def disconnect(self, code):
    pass
  
  def receive(self, text_data):
    self.send(text_data)