from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app_service'

urlpatterns = [
    path('', views.index_solicitud, name='index_solicitud'),
    path('create_solicitud/', views.create_solicitud, name='create_solicitud'),
    path('update_solicitud/<int:id>/', views.update_solicitud, name='update_solicitud'),
    path('solicitudes/delete/<int:id>/', views.delete_solicitud, name='delete_solicitud'),
    path('detalle/<int:id>/', views.details_solicitud, name='details_solicitud'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)