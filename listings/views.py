from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Property, Service
from .forms import PropertyForm, ServiceForm
from profiles.models import Profile


class PropertyDetailView(DetailView):
    model = Property
    template_name = 'property.html'
    context_object_name = 'property'


class PropertyCreateView(LoginRequiredMixin, CreateView):
    model = Property
    template_name = 'create_property.html'
    form_class = PropertyForm
    success_url = reverse_lazy('profile:profile')

    def form_valid(self, form):
        form.instance.user_profile = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


class PropertyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'update_property.html'
    form_class = PropertyForm
    success_url = reverse_lazy('profile:profile')

    def get_object(self):
        return Property.objects.get(user_profile=Profile.objects.get(user=self.request.user), pk=self.kwargs['pk'])


class PropertyDeleteView(LoginRequiredMixin, DeleteView):
    model = Property
    template_name = 'confirm.html'
    success_url = reverse_lazy('profile:profile')

    def get_object(self):
        return Property.objects.get(user_profile=Profile.objects.get(user=self.request.user), pk=self.kwargs['pk'])


class PropertySearchView(ListView):
    model = Property
    template_name = 'search_property.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        filter_conditions = {
            'address__icontains': self.request.GET.get('address', ''),
            'property_type__icontains': self.request.GET.get('property_type', ''),
            'transaction_type__icontains': self.request.GET.get('transaction_type', ''),
        }
        bhk = self.request.GET.get('bhk')
        if bhk and bhk.isdigit():
            filter_conditions['bhk'] = int(bhk)
        price = self.request.GET.get('price')
        if price and price.isdigit():
            filter_conditions['price__lte'] = int(price)
        filtered_properties = Property.objects.filter(**filter_conditions)
        data.update({'properties': filtered_properties})
        return data


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service.html'
    context_object_name = 'service'


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'create_service.html'
    success_url = reverse_lazy('profile:profile')

    def form_valid(self, form):
        form.instance.user_profile = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'update_service.html'
    success_url = reverse_lazy('profile:profile')

    def get_object(self):
        return Service.objects.get(user_profile=Profile.objects.get(user=self.request.user), pk=self.kwargs['pk'])


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    template_name = 'confirm.html'
    success_url = reverse_lazy('profile:profile')

    def get_queryset(self):
        return Service.objects.filter(user_profile=Profile.objects.get(user=self.request.user), _id=self.kwargs['pk'])


class ServiceSearchView(ListView):
    model = Service
    template_name = 'search_service.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data.update({'services': Service.objects.filter(title__icontains=self.request.GET.get('q', ''), city__icontains=self.request.GET.get('city', ''), available_location__icontains=self.request.GET.get('available_location', ''), country__icontains=self.request.GET.get('country', ''))})
        return data
