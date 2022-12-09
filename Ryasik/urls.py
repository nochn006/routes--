"""Ryasik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.http import HttpResponse
from django.urls import path, include
from pril import views

product_patterns = [
    path("", views.products2),
    path("comments", views.comments),
    path("likes", views.likes),
]

posts_patterns = [
    path('products', views.products),
    path('new', views.new),
    path('top', views.top),
]

urlpatterns = [
    path('', views.index, name="home"),
    path('posts/', include(posts_patterns)),
    path('products/', include(product_patterns)),
    path('about/', views.about, name='about'),
    path('redirect_about', views.redirect_about, name='reidrect'),
    path('redirect_contacts/', views.permanent_redirect_about, name='contacts'),
    path('not_found', views.not_found),
    path('access/<str:login>/<str:password>', views.access, name="access"),
    path('login/<str:login>/<str:password>', views.login, name="login"),
    path('json', views.json),
    path('get', views.get, name="get"),
    path('set', views.set, name="set"),
]