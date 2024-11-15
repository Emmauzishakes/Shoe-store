from django.urls import path
from . import views

app_name = "userauth"

urlpatterns = [
    path('sign-up/', views.RegistaionView, name="sign-up"),
    path('login/', views.LoginView, name="login"),
    path('logout/', views.LogoutView, name="logout"),
]
