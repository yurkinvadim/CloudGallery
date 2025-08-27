from django.urls import path

from photos.views import PhotoUploadView

app_name = 'photos'

urlpatterns = [
    path("upload/", PhotoUploadView.as_view(), name='upload'),
]