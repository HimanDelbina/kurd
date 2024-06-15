from django.urls import path
from movie import views

urlpatterns = [
    path("get_all_movie", views.get_all_movie),
    path("get_moviee_by_genre_id/<int:id>", views.get_moviee_by_genre_id),
    path("get_moviee_by_director_id/<int:id>", views.get_moviee_by_director_id),
    path("get_moviee_by_category_id/<int:id>", views.get_moviee_by_category_id),
]
