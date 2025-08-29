from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView

from photos.forms import PhotoUploadForm
from photos.models import Photo


class PhotoMixin(LoginRequiredMixin):
    model = Photo

    def get_success_url(self):
        return self.request.user.get_absolute_url()


class PhotoUploadView(PhotoMixin, CreateView):
    form_class = PhotoUploadForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PhotoUpdateView(PhotoMixin, UpdateView):
    fields = ('title', 'description')


class PhotoDeleteView(PhotoMixin, DeleteView):
    def get_queryset(self):
        return Photo.objects.filter(user=self.request.user)
