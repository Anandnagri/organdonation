"""organ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import HomePage, Register, Login, test, logoutuser, donor, reciever, about, contact, feedback, faq

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage, name="home-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name='logout'),
    path('test/', test, name='test'),
    path('donor', donor, name="donor"),
    path('reciver', reciever, name='reciver'),
    path('about', about, name='about'),
    path('contact', contact , name='contact'),
    path('feedback', feedback, name='feedback'),
    path('faq', faq, name='faq')
]
