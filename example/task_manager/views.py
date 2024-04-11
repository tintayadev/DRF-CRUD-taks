from django.shortcuts import render
from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
# Create your views here.

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = 'id'

    @action(detail=False, methods=['GET'])
    def hola(self, request):
        return Response('hola')
    
    @action(detail=False, methods=['GET'])
    def obtener_tareas_limpieza(self, request):
        '''Devuelve las tareas con el nombre limpieza'''
        tareas_limpieza = self.get_queryset.filter(nombre='Limpieza')
        serializer = self.get_serializer(tareas_limpieza, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def completadas(self, request):
        tareas_completadas = Tarea.objects.filter(completada=True)
        serializer = self.get_serializer(tareas_completadas, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['POST'])
    def crear_tarea(self, request):
        tarea_nueva = self.get_serializer(data=request.data) # Tarea
        if tarea_nueva.is_valid():
            tarea_nueva.save()
            return Response(tarea_nueva.data, status=201)
        else:
            return Response(tarea_nueva.data, status=400)

    # tareas/{id}/actualizar/
    @action(detail=True, methods=['PUT', 'PATCH'])
    def actualizar(self, request, id=None):
        tarea = self.get_object()
        serializer = self.get_serializer(tarea, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data, status=400)
    # tareas/{id}/eliminar/
    @action(detail=True, methods=['DELETE'])
    def eliminar(self, request, id=None):
        tarea = self.get_object()
        tarea.delete()
        return Response('Eliminado correctamente', status=204)

    # CRUD
    # create
    # read
    # update
    # delete