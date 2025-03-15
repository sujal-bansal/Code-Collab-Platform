from django.urls import path
from . import views

urlpatterns = [
    path('group/<str:group_name>/', views.group_view, name='group_view'),
    path('', views.homepage, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('group_list/', views.group_list, name='group-list'),
]
