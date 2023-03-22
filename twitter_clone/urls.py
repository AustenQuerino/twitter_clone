"""twitter_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from pages.views import home_view, contact_view, about_view
from profiles.views import (
    profile_detail_view, 
    profile_create_view, 
    render_initial_data, 
    dynamic_lookup_view, 
    profile_delete_view
    )

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('profile/', profile_detail_view),
    path('profile/<int:id>/', dynamic_lookup_view, name='profile'),
    path('profile/<int:id>/delete/', profile_delete_view, name='profile-delete'),
    path('create/', profile_create_view),
    path('initial/', render_initial_data),
    path('admin/', admin.site.urls),
    path('about/', about_view),
]


