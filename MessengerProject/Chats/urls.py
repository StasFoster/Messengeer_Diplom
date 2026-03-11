from django.urls import path

from .views import MainPage, SearchUser

urlpatterns = [
    path('', MainPage.as_view(), name="main"),
    path('api/chats/users/', SearchUser.as_view() ,name="api_chats"),
]
