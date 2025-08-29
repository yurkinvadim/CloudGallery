from django.urls import path

from users.views import CustomUserDetailView

app_name = 'users'

urlpatterns = [
    path('<int:pk>/', CustomUserDetailView.as_view(), name='detail'),
]