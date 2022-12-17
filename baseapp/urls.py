from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("login/", views.LoginPage, name='login'),
    path("profile/<str:pk>/", views.userProfile, name='user-profile'),
    path("register/", views.RegisterUser, name='register'),
    path("logout/", views.LogoutPage, name='logout'),
    path("", views.home, name="home"),
    path("room/<str:pk>/", views.room, name="room"),
    path("create-room", views.CreateRoom, name='create-room'),
    path("update-room/<str:pk>/", views.UpdateRoom, name='update-room'),
    path("delete-room/<str:pk>/", views.DeleteRoom, name='delete-room'),
    path("delete-message/<str:pk>/", views.DeleteMessage, name='delete-message'),
    path("edit-profile/<str:pk>/", views.UpdateProfile, name='edit-profile'),
    path("topic/", views.TopicPage, name='topic'),
    path("activity/", views.ActivityPage, name='activity'),
    path("settings/<str:pk>/", views.Setting, name='settings'),
    ]