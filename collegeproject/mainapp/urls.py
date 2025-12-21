from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('colleges/', views.colleges),
    path('infrastructure/', views.infrastructure,name='infrastructure'),
    path('placements/', views.placements,name='placements'),
    path('svecw1/',views.svecw1,name='svecw1'),
    path('vit/',views.vit,name='vit'),
    path('bvrit/',views.bvrit,name='bvrit'),
]
