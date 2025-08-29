from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cloud_gallery import settings
from cloud_gallery.views import SignUpView
from users.views import CustomUserListView

auth_urls = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(auth_urls)),
    path('', CustomUserListView.as_view(), name='user-list'),
    path('users/', include('users.urls')),
    path('photos/', include('photos.urls')),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
