from django.shortcuts import render
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import random
import string

# Create your views here.

def register_user(request):
  if request.method == 'POST':
    user_name = request.POST.get('name', None)
    user_email = request.POST.get('email', None)
    user_password = request.POST.get('password', None)
    if user_name and user_email and user_password:
      if User.objects.filter(email=user_email).exists():
        return JsonResponse({'status': 'error', 'message': 'user with email already exists'})
      else:
        user_object = User.objects.create_user(username=user_name, email=user_email, password=user_password)
        if user_object:
          return JsonResponse({'status': 'success', 'message': 'user registered successfully'})
        else:
          return JsonResponse({'status': 'error', 'message': 'user could not be registered'})
    else:
      return JsonResponse({'status': 'error', 'message': 'invalid user Name/ email/ password'})
  
  else:
    return JsonResponse({'status': 'error', 'message': 'invalid request method (only post)'})
  
def login_user(request):
  if request.method == 'POST':
    user_email = request.POST.get('email', None)
    user_password = request.POST.get('password', None)
    if user_email and user_password:
      user_object = User.objects.filter(email=user_email).first()
      auth_user = authenticate(username=user_object.username, password=user_password)
      if auth_user:
        login(request, auth_user)
        token = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(24)])
        return JsonResponse({'status': 'success', 'message': 'user loggedin successfully', 'token': token})
      else:
        return JsonResponse({'status': 'error', 'message': 'user not found'})
    else:
      return JsonResponse({'status': 'error', 'message': 'invalid email/ password'})
  
  else:
    return JsonResponse({'status': 'error', 'message': 'invalid request method (only post)'})
