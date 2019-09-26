"""Doodh_wala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from main import views as getdata_views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('getdata/', getdata_views.getdata, name='get-page'),
    path('join/', user_views.join, name='join-page'),
    path('yourdata/', getdata_views.your_data, name='yourdata-page'),

    path('signin/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='signin-page'),
    path('signout/', auth_views.LogoutView.as_view(template_name='users/signout.html'), name='signout-page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
