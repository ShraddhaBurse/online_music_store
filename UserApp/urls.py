from django.urls import path,include
from UserApp import views

urlpatterns = [
    path('', views.home),
    path('PlaySong/<sid>',views.PlaySong),
    path('SignUp',views.SignUp),
    path('Login',views.Login),
    path('Logout',views.Logout),
]
