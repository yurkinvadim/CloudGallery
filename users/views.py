import io
import zipfile

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView

from photos.models import Photo
from users.models import CustomUser


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    context_object_name = 'users'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(photos__isnull=False).distinct()
        return qs

class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    context_object_name = 'user'


class UserPhotosDownloadView(LoginRequiredMixin, View):
    # TODO: Implement photo download via Celery for users with many photos
    # Create a Celery task to generate the zip archive
    # Save the zip file to a cloud storage

    def get(self, request, pk):
        owner = get_object_or_404(CustomUser, pk=pk)
        photos = Photo.objects.filter(user=owner)
        if not photos.exists():
            return HttpResponse("User has no photos", content_type="text/plain")

        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as zip_file:
            for photo in photos:
                filename = photo.image.name.split("/")[-1]
                zip_file.writestr(filename, photo.image.read())

        buffer.seek(0)
        response = HttpResponse(buffer, content_type="application/zip")
        response["Content-Disposition"] = f'attachment; filename="{owner.username}_photos.zip"'
        return response