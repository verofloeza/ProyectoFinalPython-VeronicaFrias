from django.shortcuts import render, redirect, get_object_or_404
from service.forms import  SolicitudForm
from service.models import  SolicitudServicio
from django.utils.dateparse import parse_date
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse


def index_solicitud(request):
    query_nombre = request.GET.get('q', '')
    query_fecha = request.GET.get('fecha', '')

    solicitudes = SolicitudServicio.objects.all()

    if query_nombre:
        solicitudes = solicitudes.filter(
            Q(nombre__icontains=query_nombre) | 
            Q(descripcion__icontains=query_nombre)
        )
    
    if query_fecha:
        try:
            fecha_filtro = parse_date(query_fecha)
            if fecha_filtro:
                solicitudes = solicitudes.filter(fecha_solicitud=fecha_filtro)
        except ValueError:
            pass
    
    paginator = Paginator(solicitudes, 10) 
    page = request.GET.get('page')
    
    try:
        solicitudes = paginator.page(page)
    except PageNotAnInteger:
        solicitudes = paginator.page(1)
    except EmptyPage:
        solicitudes = paginator.page(paginator.num_pages)
    
    return render(request, 'service/solicitud_servicio.html', {
        'solicitudes': solicitudes,
        'query_nombre': query_nombre,
        'query_fecha': query_fecha
    })

def create_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                solicitud = form.save(commit=False)
                solicitud.usuario = request.user
                solicitud.save()
                return redirect('app_service:index_solicitud')
            except Exception as e:
                print(f"Error al guardar la solicitud: {e}") 
        else:
            print(form.errors)  
    else:
        form = SolicitudForm()
    
    context = {'form': form}
    return render(request, 'service/create_solicitud.html', context)

def delete_solicitud(request, id):
    try:
        solicitud = get_object_or_404(SolicitudServicio, id=id)
        solicitud.delete()
        return JsonResponse({'status': 'success'}, status=200)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
def update_solicitud(request, id):
    solicitud = get_object_or_404(SolicitudServicio, id=id)
    
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES, instance=solicitud)
        print("FILES:", request.FILES)  
        print("POST:", request.POST)  
        
        if form.is_valid():
            if 'foto' in request.FILES:
                print("Nueva foto encontrada")
                if solicitud.foto:
                    try:
                        import os
                        if os.path.exists(solicitud.foto.path):
                            os.remove(solicitud.foto.path)
                    except Exception as e:
                        print(f"Error al eliminar foto anterior: {e}")

                solicitud.foto = request.FILES['foto']
            
            solicitud.save()
            print(f"Solicitud guardada. Foto: {solicitud.foto}")
            return redirect('app_service:index_solicitud')
        else:
            print("Form errors:", form.errors)
    else:
        form = SolicitudForm(instance=solicitud)
    
    return render(request, 'service/update_solicitud.html', {
        'form': form,
        'solicitud': solicitud
    })

def details_solicitud(request, id):
    solicitud = get_object_or_404(SolicitudServicio, id=id)
    return render(request, 'service/details_solicitud.html', {'solicitud': solicitud})