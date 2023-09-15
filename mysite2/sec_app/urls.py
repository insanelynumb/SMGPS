from django.urls import path
from sec_app import views
app_name = 'sec_app'
urlpatterns=[
    path('formpage/', views.users, name='users'),
    path('home/', views.index, name='index'),
    path('register/', views.register, name='register'),

]