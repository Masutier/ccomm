from django.urls import path, include
from . import views


urlpatterns = [
    path('caps', views.caps, name='path'),
    path('createCap', views.createCap, name='createCap'),
    path('updateOther/<str:pk>', views.updateOther, name='updateOther'),
    path('delother/<str:pk>', views.delother, name='delother'),
    
]
