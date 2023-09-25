from django.shortcuts import render
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import random
import string

from .models import *

# Create your views here.

def register_user(request):
  if request.method == 'POST':
    user_name = request.POST.get('name', None)
    user_email = request.POST.get('email', None)
    user_password = request.POST.get('password', None)
    # check for null fields
    if user_name and user_email and user_password:
      # check if user already exists
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
    # check for null fields
    if user_email and user_password:
      user_object = User.objects.filter(email=user_email).first()
      auth_user = authenticate(username=user_object.username, password=user_password)
      if auth_user:
        user_token_object = UserToken.objects.filter(user=user_object, status=True)
        
        # check if user is already logged in
        if user_token_object.exists():
          return JsonResponse({'status': 'error', 'message': 'user already logged in'})
        else:
          login(request, auth_user)
          auth_token = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(24)])
          
          user_token_object = UserToken.objects.filter(user=user_object)
          # check if it is user's first login
          if user_token_object.exists():
            user_token_object = user_token_object.first()
          else:
            user_token_object = UserToken()
            
          user_token_object.set_user_token(user=user_object, token=auth_token, status=True)
          user_token_object.save()
          return JsonResponse({'status': 'success', 'message': 'user loggedin successfully', 'token': auth_token})
      else:
        return JsonResponse({'status': 'error', 'message': 'user not found'})
    else:
      return JsonResponse({'status': 'error', 'message': 'invalid email/ password'})
  
  else:
    return JsonResponse({'status': 'error', 'message': 'invalid request method (only post)'})


def logout_user(request):
  if request.method == 'POST':
    auth_token = request.headers.get('token')
    user_token_object = UserToken.objects.filter(token=auth_token).first()
    if user_token_object.status:
      user_token_object.status = False
      user_token_object.save()
      logout(request)
      return JsonResponse({'status': 'success', 'message': 'user logged out successfully'})
    else:
      return JsonResponse({'status': 'error', 'message': 'no user is logged in currently'})
  else:
    return JsonResponse({'status': 'error', 'message': 'invalid request method (only post)'})