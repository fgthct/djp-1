from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login', views.custom_login, name='login'),
    path('logout', views.custom_logout, name='logout'),
    path('profile/<username>', views.profile, name='profile'),   
]

""" urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    # path('profile/', views.profile, name='profile'),   
] """
