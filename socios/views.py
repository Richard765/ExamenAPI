from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Socio

@api_view(['POST'])
def crear_socio(request):
    dni = request.data.get('dni')
    numero_socio = request.data.get('numero_socio')
    contraseña = request.data.get('contraseña')
    socio = Socio(dni=dni, numero_socio=numero_socio, contraseña=contraseña)
    socio.save()
    return Response({'mensaje': 'Socio creado correctamente'}, 201)

@api_view(['POST'])
def modificar_contraseña(request, id):
    contraseña_nueva = request.data.get('contraseña')
    socio = get_object_or_404(Socio, id=id)
    socio.contraseña = contraseña_nueva
    socio.save()
    return Response({'mensaje': 'Contraseña del socio modificada correctamente'})


@api_view(['GET'])
def lista_socios(request):
    socios = Socio.objects.all()
    data = [{'dni': socio.dni, 'numero_socio': socio.numero_socio, 'contraseña': socio.contraseña} for socio in socios]
    return Response(data)