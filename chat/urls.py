from django.contrib import admin
from django.urls import path
from chat import views

urlpatterns = [
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('', views.home, name='home'),
    path('about.html', views.about, name="aboutme")
]