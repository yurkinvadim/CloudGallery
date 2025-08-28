from django.urls import path

from photos.views import PhotoUploadView, PhotoDeleteView

app_name = "photos"

urlpatterns = [
    path("upload/", PhotoUploadView.as_view(), name="upload"),
    path("delete/<int:pk>/", PhotoDeleteView.as_view(), name="delete"),
]