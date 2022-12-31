from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, CreateProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView
from .models import Profile

# Create your views here.
class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('home')

class EditProfileView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    
    fields = ['bio', 'profile_pic', 'facebook_url', 'instagram_url', 'twitter_url', 'pinterest_url']
    success_url = reverse_lazy('home')

class CreateProfileView(CreateView):
    model = Profile
    template_name = 'registration/create_profile.html'
    
    form_class = CreateProfileForm
    # fields = ['bio', 'profile_pic', 'facebook_url', 'instagram_url', 'twitter_url', 'pinterest_url']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def password_success(request):
    return render(request, 'registration/password_success.html', {})