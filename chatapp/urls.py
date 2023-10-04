from django.urls import re_path, path

from . import consumers
from . import views

websocket_urlpatterns = [
  re_path(r'api/chat/send/', consumers.ChatConsumer.as_asgi()),
]

urlpatterns = [
  path('', view=views.index, name='index'),
  path('register/', view=views.register_user, name='register'),
  path('login/', view=views.login_user, name='login'),
  path('home/', view=views.home, name='home'),
  path('logout/', view=views.logout_user, name='logout'),
  path('online-users/', view=views.get_online_users, name='online_users'),
  path('chat/start/', view=views.start_chat, name='start_chat'),
]