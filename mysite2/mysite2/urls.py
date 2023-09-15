"""
URL configuration for mysite2 project.

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
from sec_app import views
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name='user_login'),
    path('sec_app/', include('sec_app.urls')),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special'),
    path('verify/<int:movement_id>/', views.verify_action, name='verify_action'),
    path('reject/<int:movement_id>/', views.reject_action, name='reject_action'),

]
