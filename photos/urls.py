from django.urls import path

from photos.views import PhotoDeleteView, PhotoUpdateView, PhotoUploadView

app_name = "photos"

urlpatterns = [
    path("upload/", PhotoUploadView.as_view(), name="upload"),
    path("<int:pk>/delete/", PhotoDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", PhotoUpdateView.as_view(), name="update"),
]
