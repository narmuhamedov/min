from django.urls import path
from . import views

urlpatterns = [
    path('web_hello/', views.hello_world, name='hello'),
    path('med_post/', views.med_blog_all, name='med_post'),
]
