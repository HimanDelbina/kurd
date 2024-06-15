from django.urls import path
from user import views

urlpatterns = [
    path("create_user", views.create_user),
    path("login_user", views.login_user),
    path("delete_user_by_id/<int:id>", views.delete_user_by_id),
    path("edit_user", views.edit_user),
    path("get_all_user", views.get_all_user),
]
