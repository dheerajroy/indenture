from django.urls import path
from .views import CreateProfileView, UpdateProfileView, ProfileDetailView

app_name = 'profile'

urlpatterns = [
    path('', ProfileDetailView.as_view(), name='profile'),
    path('create', CreateProfileView.as_view(), name='create'),
    path('update', UpdateProfileView.as_view(), name='update'),
]