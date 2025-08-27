from django.urls import reverse
from django.views.generic import CreateView

from photos.forms import PhotoUploadForm
from photos.models import Photo


class PhotoUploadView(CreateView):
    model = Photo
    form_class = PhotoUploadForm

    def get_success_url(self):
        return reverse( 'user-detail',kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

