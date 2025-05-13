from django.urls import path
from . import views

urlpatterns = [
       path('hackerrank-news/', views.hackerrank_news, name='hackerrank_news'),
]

