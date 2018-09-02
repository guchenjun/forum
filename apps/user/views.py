from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile
from apps.category.models import BBS
from .forms import RegisterForm, LoginForm

# Create your views here.


def index(request):
    return render(request, "index.html")


def register(request):
    method = request.method
    if method == 'POST':
        form = RegisterForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        result = form.check_data(username, password)
        if result == 'suc':
            user = User.objects.create_user(username=username, password=password)
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponse("注册成功!")
        else:
            return HttpResponse(result)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    method = request.method
    if method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponse("登录成功!")
            else:
                # 登录失败
                return HttpResponse("登录失败!")
    return render(request, 'login.html')


def forum(request):
    users_info = UserProfile.objects.last()
    users_info.user_count = UserProfile.objects.count()
    users_info.thread_count = BBS.objects.count()
    if request.user.id:
        userProfile = UserProfile.objects.get(user_id=request.user.id)
        return render(request, "forum.html", {'userProfile': userProfile, 'users_info': users_info})
    else:
        return render(request, "forum.html",{"users_info": users_info})
