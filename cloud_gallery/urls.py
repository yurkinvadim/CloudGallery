from django.contrib import admin
from django.urls import path, include

from cloud_gallery.views import SignUpView

auth_urls = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(auth_urls)),
]
