from django.urls import path , include
from themedia import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("test/", views.Test_media_done),
    path("test/done/", views.Test_media),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)