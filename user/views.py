from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomUserChangeForm, UserCreationFormWithEmail, ProfileChangeForm
from django.contrib.auth import logout
from .models import Profile

class UserLoginViews(LoginView):
    template_name = "user/login.html"


class RegisterView(View):
    template_name = "user/register.html"

    def get(self, request):
        form = UserCreationFormWithEmail()
        return render(request, 'app_user:register', {'form': form})

    def post(self, request):
        form = UserCreationFormWithEmail(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_user:login')
        return render(request, 'app_user:register', {'form': form})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'user/edit-profile.html'
    success_url = reverse_lazy('app_user:edit-profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileChangeForm(instance=profile)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  
        
        user_form = self.get_form() 
        profile = Profile.objects.get(user=self.request.user)  
        profile_form = ProfileChangeForm(request.POST, request.FILES, instance=profile)  

        if user_form.is_valid() and profile_form.is_valid():

            print("User form is valid:", user_form.cleaned_data)
            print("Profile form is valid:", profile_form.cleaned_data)

            user_form.save()
            profile_form.save()
            return redirect(self.success_url)
        else:
            print("User form errors:", user_form.errors)
            print("Profile form errors:", profile_form.errors)
            
        return self.render_to_response(
            self.get_context_data(form=user_form, profile_form=profile_form)
        )

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user/password_change.html' 
    success_url = reverse_lazy('app_user:profile')  

    def form_valid(self, form):
        return super().form_valid(form)  
     
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('app_user:login')
