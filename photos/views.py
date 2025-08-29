from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView

from photos.forms import PhotoUploadForm
from photos.models import Photo


class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoUploadForm

    def get_success_url(self):
        return self.request.user.get_absolute_url()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ('title', 'description')

    def get_success_url(self):
        return self.request.user.get_absolute_url()

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo

    def get_queryset(self):
        return Photo.objects.filter(user=self.request.user)

    def get_success_url(self):
        return self.request.user.get_absolute_url()
