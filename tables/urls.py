"""easytables URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from tables import views

urlpatterns = [
    path('show_flights_routes', views.show_flights_routes, name='show_flights_routes'),
    path('show_planes', views.show_planes, name='show_planes'),
    path('login/', views.login_page, name='login_page'),
    path('registration/', views.registration_page, name='registration_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('password/', views.PasswordChangedView.as_view(template_name='change_password.html'), name='password_change'),
    path('password_success/', views.password_success, name='password_success'),
    path('add_plane/', views.add_plane, name='add_plane'),
    path('add_flights_routes/', views.add_flights_routes, name='add_flights_routes'),
]
