from django.urls import path

from users.views import UserDetailView, UserPhotosDownloadView

app_name = 'users'

urlpatterns = [
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('<int:pk>/download_photos/', UserPhotosDownloadView.as_view(), name='download_photos'),
]