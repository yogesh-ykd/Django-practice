from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('sayhello/', views.say_hello)
]