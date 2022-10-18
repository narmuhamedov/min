from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('registration/', views.Registration.as_view(), name='registr'),
    path('login/', views.NewLoginForm.as_view(), name='login'),
    path('login_list/', views.UserListView.as_view(), name='userlist'),
]
