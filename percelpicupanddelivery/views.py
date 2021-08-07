from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import View, CreateView, ListView
from django.urls import reverse_lazy
from django.conf import settings
from accounts.views import HubManagerRequiredMixin
from .forms import PercelPicUpForm, PercelDeliveryForm

from .models import PercelPicUp, PercelDelivery

class PicupAndDeliveryListView(HubManagerRequiredMixin, View):
    template_name = 'percels/picup-and-delivery-list.html'
    def get(self, request, *args, **kwargs):
        picup_percels = PercelPicUp.objects.all()
        delivey_percels = PercelDelivery.objects.all()
        context = {
            'picup_percels': picup_percels,
            'delivery_percels': delivey_percels
        }
        return render(request, self.template_name, context)

class PercelPicupList(HubManagerRequiredMixin, ListView):
    model = PercelPicUp
    template_name = 'percels/picup-percel-list.html'
    
    def get_queryset(self, *args, **kwargs):
        qs = super(PercelPicupList, self).get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs

class PercelPicUpCreateView(HubManagerRequiredMixin, CreateView):
    model = PercelPicUp
    template_name = 'percels/percel_picup.html'
    form_class = PercelPicUpForm 
    success_url = reverse_lazy('percel:home_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.percel.is_active = False
        return super(PercelPicUpCreateView, self).form_valid(form)

class PercelDeliveryList(HubManagerRequiredMixin, ListView):
    model = PercelDelivery
    template_name = 'percels/delivery-percel-list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(PercelDeliveryList, self).get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs

class PercelDeliveryCreateView(HubManagerRequiredMixin, CreateView):
    model = PercelDelivery
    template_name = 'percels/percel_delivery.html'
    form_class = PercelDeliveryForm 
    success_url = reverse_lazy('percel:home_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PercelDeliveryCreateView, self).form_valid(form)

