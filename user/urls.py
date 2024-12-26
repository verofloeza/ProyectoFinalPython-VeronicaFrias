from django.urls import path
from . import views

app_name = 'app_user'

urlpatterns = [
    path('login/', views.UserLoginViews.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register' ),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('edit-profile/', views.ProfileUpdateView.as_view(), name='edit-profile'),
    path('password-change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
]
