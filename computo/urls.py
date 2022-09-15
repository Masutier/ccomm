from django.urls import path, include
from . import views


urlpatterns = [
    path('pcs', views.pcs, name='pcs'),
    path('cpu', views.cpu, name='cpu'),
    path('laptop', views.laptop, name='laptop'),
    path('createPc', views.createPc, name='createPc'),
    path('updatePc/<str:pk>', views.updatePc, name='updatePc'),
    path('delpc/<str:pk>', views.delpc, name='delpc'),

    
]
