from functools import cached_property

from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from photos.models import Photo


class CustomUser(AbstractUser):

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})


    @cached_property
    def last_photo(self) -> Photo:
        return self.photos.first()
