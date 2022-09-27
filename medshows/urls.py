from django.urls import path
from . import views

urlpatterns = [
    path('medshows/', views.MedShowListView.as_view(), name='medshow'),
    path('medshows/<int:id>/', views.MedShowsDetailView.as_view(), name='medshows_detail'),
    path('medshows/<int:id>/update/', views.MedShowUpdateView.as_view(), name='medshows_update'),
    path('medshows/<int:id>/delete/', views.MedShowsDeleteView.as_view(), name='medshows_delete'),
    path('add-shows/', views.MedShowsCreateView.as_view(), name='medShow'),
]
