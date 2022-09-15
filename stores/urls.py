from django.urls import path, include
from . import views


urlpatterns = [
    path('stores', views.stores, name='stores'),
    path('createStore', views.createStore, name='createStore'),
    path('updateStore/<str:pk>', views.updateStore, name='updateStore'),
    
]
