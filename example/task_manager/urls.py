from rest_framework.routers import DefaultRouter
from .views import TareaViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('tareas', TareaViewSet)

urlpatterns = [
    path('', include(router.urls))
]



# api/estudiante/<id>/eliminar