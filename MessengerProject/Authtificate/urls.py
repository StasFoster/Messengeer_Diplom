from django.urls import path

from .views import RegisterViews, LoginViews, user_logout

urlpatterns = [
    path("register/", RegisterViews.as_view(), name="register"),
    path("login/", LoginViews.as_view(), name="login"),
    path("logout/", user_logout, name="logout"),
]
