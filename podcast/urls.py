from django.urls import path
from podcast import views

urlpatterns = [
    path("get_all_podcast_video", views.get_all_podcast_video),
    path("get_all_podcast_mp3", views.get_all_podcast_mp3),
    path(
        "get_all_podcast_mp3_by_category_id/<int:id>",
        views.get_all_podcast_mp3_by_category_id,
    ),
    path(
        "get_all_podcast_video_by_category_id/<int:id>",
        views.get_all_podcast_video_by_category_id,
    ),
    path(
        "get_all_podcast_mp3_by_signer_id/<int:id>",
        views.get_all_podcast_mp3_by_signer_id,
    ),
    path(
        "get_all_podcast_video_by_signer_id/<int:id>",
        views.get_all_podcast_video_by_signer_id,
    ),
]
