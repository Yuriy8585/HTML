from django.urls import include, path
from hello import views

urlpatterns = [
    path("", include("hello.urls")),
    path("", views.home, name="home"),
]