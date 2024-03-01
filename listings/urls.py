from django.urls import path
from .views import PropertyCreateView, PropertyUpdateView, PropertyDetailView, PropertyDeleteView, PropertySearchView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView, ServiceSearchView

app_name = 'listing'

urlpatterns = [
    path('property/<int:pk>', PropertyDetailView.as_view(), name='property'),
    path('property/create', PropertyCreateView.as_view(), name='create_property'),
    path('property/update/<int:pk>', PropertyUpdateView.as_view(), name='update_property'),
    path('property/delete/<int:pk>',PropertyDeleteView.as_view(), name='delete_property'),
    path('property/search', PropertySearchView.as_view(), name='search_property'),
    path('service/create', ServiceCreateView.as_view(), name='create_service'),
    path('service/update/<int:pk>', ServiceUpdateView.as_view(), name='update_service'),
    path('service/delete/<int:pk>', ServiceDeleteView.as_view(), name='delete_service'),
    path('service/search', ServiceSearchView.as_view(), name='search_service')
]