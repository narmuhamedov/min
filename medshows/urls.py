from django.urls import path
from . import views

urlpatterns = [
    path('medshows/', views.show_all_med, name='medshow'),
    path('medshows/<int:id>/', views.show_all_med_detail, name='medshows_detail'),
    path('medshows/<int:id>/update/', views.show_update, name='medshows_update'),
    path('medshows/<int:id>/delete/', views.show_delete, name='medshows_delete'),
    path('add-shows/', views.add_med_shows, name='medShow'),
]
