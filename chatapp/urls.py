from django.urls import re_path, path

from . import consumers
from . import views

websocket_urlpatterns = [
  re_path(r'ws/chat/', consumers.ChatConsumer.as_asgi()),
]

urlpatterns = [
  path('register_user/', view=views.register_user, name='register'),
  path('login_user/', view=views.login_user, name='login'),
  path('logout_user/', view=views.logout_user, name='logout'),
]