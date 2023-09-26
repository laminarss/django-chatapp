from django.urls import re_path, path

from . import consumers
from . import views

websocket_urlpatterns = [
  re_path(r'api/chat/send/', consumers.ChatConsumer.as_asgi()),
]

urlpatterns = [
  path('api/register/', view=views.register_user, name='register'),
  path('api/login/', view=views.login_user, name='login'),
  path('api/logout/', view=views.logout_user, name='logout'),
  path('api/online-users/', view=views.get_online_users, name='online_users'),
  path('api/chat/start/', view=views.start_chat, name='start_chat'),
]