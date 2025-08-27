from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

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

