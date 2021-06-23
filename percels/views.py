from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import View, CreateView, ListView
from django.urls import reverse_lazy
from django.conf import settings
from accounts.models import Account
from accounts.views import StaffRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PercelForm

from .models import Percel

class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

class PercelListview(StaffRequiredMixin, ListView):
    model = Percel
    template_name = 'percels/percel-list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(PercelListview, self).get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs

class PercelCreateView(StaffRequiredMixin, CreateView):
    model = Percel
    template_name = 'percels/create_percel.html'
    form_class = PercelForm

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        user = Account.objects.get(pk=current_user.pk)
        context = super(PercelCreateView, self).get_context_data(**kwargs)
        context['form'].fields['picuplocation'].queryset = PicupLocation.objects.filter(user_id=user.id)

    # def get_form_kwargs(self):
    #     kwargs = super(PercelCreateView, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs

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

