from django.urls import re_path, path

from . import consumers
from . import views

websocket_urlpatterns = [
  re_path(r'ws/chat/', consumers.ChatConsumer.as_asgi()),
]

urlpatterns = [
  path('api/register/', view=views.register_user, name='register'),
  path('api/login/', view=views.login_user, name='login'),
  path('api/logout/', view=views.logout_user, name='logout'),
]