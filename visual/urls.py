from django.urls import path, include
from . import views


urlpatterns = [
    path('monitors', views.monitors, name='monitors'),
    path('createMonitor', views.createMonitor, name='createMonitor'),
    path('updateMonitor/<str:pk>', views.updateMonitor, name='updateMonitor'),
    path('delMonitor/<str:pk>', views.delMonitor, name='delMonitor'),
    
]
