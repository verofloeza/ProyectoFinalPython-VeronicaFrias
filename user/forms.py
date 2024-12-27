from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Coloque su email.')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationFormWithEmail, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birth_date', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ProfileChangeForm(ProfileForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birth_date', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control', 'value': ''}),
        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

