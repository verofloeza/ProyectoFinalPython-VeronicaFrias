from django.urls import path
from django.conf.urls import handler404
from . import views

handler404 = views.custom_page_not_found_view

app_name = 'app_home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about , name='about' )
]
