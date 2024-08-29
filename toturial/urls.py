from django.urls import path
from toturial import views

urlpatterns = [
    path("get_all_toturial", views.get_all_toturial),
]
