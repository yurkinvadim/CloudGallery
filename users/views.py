from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from users.models import CustomUser


class CustomUserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    context_object_name = 'users'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(photos__isnull=False).distinct()
        return qs

class CustomUserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    context_object_name = 'user'

