from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView
from django.urls import reverse_lazy
from django.conf import settings
from accounts.models import Account
from accounts.views import StaffRequiredMixin
from .forms import PercelForm

from .models import PicupLocation


class PicupLocationListview(StaffRequiredMixin, ListView):
    model = PicupLocation
    template_name = 'percels/picuplocation-list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(PicupLocationListview, self).get_queryset(*args, **kwargs)

class PicupLocationCreateView(StaffRequiredMixin, CreateView):
    model = PicupLocation
    template_name = 'percels/create_picuplocation.html'
    form_class = PicupLocationForm 
    success_url = reverse_lazy('percel:home_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PicupLocationCreateView, self).form_valid(form)
