from django.urls import path
from . import views

app_name = "mainApp"   

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.register_request, name="login"),
    path("logout", views.logout_request, name= "logout"),

]