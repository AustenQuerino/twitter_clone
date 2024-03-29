from django.urls import path
from .views import (
    profile_list_view,
    ProfileListView,
    profile_create_view, 
    ProfileCreateView,
    profile_update_view,
    ProfileUpdateView,
    profile_detail_view, 
    ProfileDetailView,
    profile_delete_view,
)

app_name='profiles'
urlpatterns = [
    # path('', profile_list_view, name='profile-list'),
    path('', ProfileListView.as_view(), name='profile-list'),
    # path('create/', profile_create_view, name='profile-create'),
    path('create/', ProfileCreateView.as_view(), name='profile-create'),
    # path('<int:id>/', profile_detail_view, name='profile-detail'),
    path('<int:id>/', ProfileDetailView.as_view(), name='profile-detail'),
    # path('<int:id>/update/', profile_update_view, name='profile-update'),
    path('<int:id>/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('<int:id>/delete/', profile_delete_view, name='profile-delete'),
]
