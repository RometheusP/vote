"""vote URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path

from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_subjects),
    path('teachers/', views.show_teachers),
    path('excel/', views.export_teachers_excel),
    path('teachers_data/', views.get_teachers_data),
    path('praise/', views.praise_or_criticize),
    path('criticize/', views.praise_or_criticize),
    path('login.html', views.log),
    path('captcha/', views.get_captcha),
    path('login/', views.get_captcha),
]
