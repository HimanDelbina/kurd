from django.urls import path
from myshow import views

urlpatterns = [
    path("get_all_show", views.get_all_show),
    path("get_show_by_genre_id/<int:id>", views.get_show_by_genre_id),
    path("get_show_by_director_id/<int:id>", views.get_show_by_director_id),
    path("get_show_by_category_id/<int:id>", views.get_show_by_category_id),
]
