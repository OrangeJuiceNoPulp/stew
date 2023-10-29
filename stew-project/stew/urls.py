"""
URL configuration for stew project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #STEW
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('createcourse/', views.createcourse, name='createcourse'),
    path('joincourse/', views.joincourse, name='joincourse'),
    path('course/<int:course_pk>/', views.coursehome, name='coursehome'),
    path('faq/', views.faq, name='faq'),
    
    #Account Management
    path('logout/', views.logoutaccount, name='logoutaccount'),
    path('login/', views.loginaccount, name='loginaccount'),
    path('signup/', views.signupaccount, name='signupaccount'),
    path('user/<int:user_pk>/', views.userprofile, name='userprofile'),
]
