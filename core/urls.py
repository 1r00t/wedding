from distutils.version import LooseVersion
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from core import views


urlpatterns = [
    path("", include("gallery.urls")),
    path("login/", views.login_user, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
