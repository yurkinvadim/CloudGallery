from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from users.models import CustomUser


class CustomUserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    context_object_name = 'users'


class CustomUserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    context_object_name = 'user'

