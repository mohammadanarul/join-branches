from django.shortcuts import render, HttpResponse
from django.views.generic import View, CreateView
from django.urls import reverse_lazy
from .forms import (
    AreaLocationForm,
    PicupLocationForm,
    PercelForm,
    PercelPicUpAndDeliveryForm,
)

from .models import (
    AreaLocation,
    PicupLocation,
    Percel,
    PercelPicUpAndDelivery
)

def home_page_view(request):
    return HttpResponse('<h1>Welcome</h1>')

class AreaLocationCreateView(CreateView):
    model = AreaLocation
    template_name = 'percels/create_arealocation.html'
    form_class = AreaLocationForm 
    success_url = reverse_lazy('percel:home_page')

class PicupLocationCreateView(CreateView):
    model = PicupLocation
    template_name = 'percels/create_picuplocation.html'
    form_class = PicupLocationForm 
    success_url = reverse_lazy('percel:home_page')
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
    
'''
def percel_create_view(request):
    if request.method == 'POST':
        form = PercelForm(request.POST, request.user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('percel:home_page')
    else:
        form = PercelForm(request.user)
    template_name = 'percels/create_percel.html'
    return render(request, template_name, {'form': form})


class PercelPicUpAndDeliveryCreateView(CreateView):
    model = PercelPicUpAndDelivery
    template_name = 'percels/create_percel_picup_and_delivery.html'
    form_class = PercelPicUpAndDeliveryForm 
    success_url = reverse_lazy('percel:home_page')

