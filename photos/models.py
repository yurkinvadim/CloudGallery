from django.db import models

from cloud_gallery.settings import AUTH_USER_MODEL


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.user.id, filename)

class Photo(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to=user_directory_path)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f'Photo {self.id}'

    class Meta:
        ordering = ['-uploaded_at']