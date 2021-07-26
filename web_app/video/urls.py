from django.urls import path
from . import views

urlpatterns = [
    path('', views.signIn),
    path('upload/', views.upload),
    path('register/', views.register),
    path('login/', views.signIn, name = "login"),
    path('home/', views.index, name = 'home'),
    path('logout/', views.disconnect, name = 'logout')
]
