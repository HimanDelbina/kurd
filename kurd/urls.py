from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth", views.obtain_auth_token),
    path("api-auth", include("rest_framework.urls")),
    path("user/", include("user.urls")),
    path("movie/", include("movie.urls")),
    path("music/", include("music.urls")),
    path("myshow/", include("myshow.urls")),
    path("toturial/", include("toturial.urls")),
    path("podcast/", include("podcast.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "KURD PLUS"
