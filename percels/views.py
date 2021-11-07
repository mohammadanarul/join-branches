from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import View, CreateView, ListView, FormView
from django.urls import reverse_lazy
from django.conf import settings
from accounts.models import Account
from accounts.views import HubManagerRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from picuplocations.models import PicupLocation
from .forms import PercelForm
from .unique_percel_generator import unique_random_string_generator

from .models import Percel

class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

class PercelListview(HubManagerRequiredMixin, ListView):
    model = Percel
    template_name = 'percels/percel-list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(PercelListview, self).get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs

class PercelCreateView(HubManagerRequiredMixin, CreateView):
    model = PicupLocation
    template_name = 'percels/create_percel.html'
    form_class = PercelForm
    success_url = reverse_lazy('percel:home_page')

    def get_initial(self, *args, **kwargs):
        initial = super(PercelCreateView, self).get_initial(**kwargs)
        initial['picuplocation'] = PicupLocation.objects.filter(user=self.request.user)
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(
            self.request,
            'add percel your profile.'
        )
        return super(PercelCreateView, self).form_valid(form)



       

from django.forms import formset_factory, modelformset_factory

'''
def percel_create_view(request):
    PercelFormSet = modelformset_factory(Percel, fields=(
        "picuplocation",
        "customer_name",
        "customer_phone_number",
        "customer_address",
        "product_weight",
        "area_location",
        "product_price",
        "customerdetails",
    ), extra=0)
    data = request.POST or None
    formset = PercelFormSet(data=data, queryset=Percel.objects.filter(user=request.user))
    for form in formset:
        form.fields['picuplocation'].queryset = PicupLocation.objects.filter(user=request.user)
    
    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('/')
    template_name = 'percels/create_percel.html'
    return render(request, template_name, {'formset': formset})

def percel_create_view(request):
    if request.method == 'POST':
        form = PercelForm(request.POST, request.user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('percel:home_page')
    else:
        form = PercelForm()
    template_name = 'percels/create_percel.html'
    return render(request, template_name, {'form': form})
'''

