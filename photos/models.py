import os

from django.db import models
from django.utils.timezone import now

from cloud_gallery.settings import AUTH_USER_MODEL


def upload_to_user_directory_with_timestamp(instance, filename):
    ext = filename.split('.')[-1]
    return f'user_{instance.user.id}/{now().strftime("%Y%m%d%H%M%S")}.{ext}'


class Photo(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to=upload_to_user_directory_with_timestamp)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f'Photo {self.id}'

    class Meta:
        ordering = ['-uploaded_at']

    def delete(self, *args, **kwargs):
        # Delete from media folder
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)