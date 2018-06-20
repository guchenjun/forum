"""testDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from apps.user import views
from apps.category.views import logout, category, post, reply, thread
from apps.bank.views import bank, deposit, withdraw, transfer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('reg/', views.register),
    path('login/', views.login),
    path('forum/', views.forum),
    path('forum/logout/', logout),
    re_path('forum/f(\d+)/', category),
    re_path('forum/r(\d+)/', thread),
    re_path('forum/p(?P<bbs_id>\d+)/post/', post),
    path('forum/reply/', reply),
    path('forum/plugins/bank/', bank),
    path('forum/plugins/bank/deposit/', deposit),
    path('forum/plugins/bank/withdraw/', withdraw),
    path('forum/plugins/bank/transfer/', transfer)
]
