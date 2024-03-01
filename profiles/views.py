from django.db.models.base import Model as Model
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileForm
from listings.models import Property, Service


class CreateProfileView(CreateView, LoginRequiredMixin):
    form_class = ProfileForm
    template_name = 'create_profile.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class UpdateProfileView(UpdateView):
    form_class = ProfileForm
    template_name = 'update_profile.html'
    success_url = '/'

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data.update({'properties': Property.objects.filter(user_profile=Profile.objects.get(user=self.request.user)),
                    'services': Service.objects.filter(user_profile=Profile.objects.get(user=self.request.user))})
        return data
