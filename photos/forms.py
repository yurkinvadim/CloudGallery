from django import forms

from photos.models import Photo


class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'description', 'image')
