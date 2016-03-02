from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def login_view(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('feature_requests/login.html', c)

def auth_and_login(request, onsuccess='../', onfail='feature_requests/login.html'):
    password = request.POST['password'] if 'password' in request.POST else request.POST['password1']
    user = authenticate(username=request.POST['email'], password=password)
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return render(request, onfail, {
        'error_text' : 'Failed to login'
        })

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True

def sign_up_in(request):
    post = request.POST
    error_text = ""
    if not user_exists(post['email']):
        user = create_user(username=post['email'], email=post['email'], password=post['password1'])
        return auth_and_login(request)
    else:
        error_text = 'User already exists'
        return render(request, 'feature_requests/login.html', {
        'error_text' : error_text
        })
