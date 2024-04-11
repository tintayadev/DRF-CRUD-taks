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

    @action(detail=False, methods=['GET'])
    def hola(self, request):
        return Response('hola')
    
    @action(detail=False, methods=['GET'])
    def obtener_tareas_limpieza(self, request):
        '''Devuelve las tareas con el nombre limpieza'''
        tareas_limpieza = Tarea.objects.filter(nombre='Limpieza')
        serializer = self.get_serializer(tareas_limpieza, many=True)
        return Response(serializer.data)
    
    # TO DO: realiza el nuevo endpoint GET: completadas/