from django.contrib import admin
from django.urls import path, include
from . import views

from rest_framework import routers
from desafio.api import viewsets as desafioviewsets
from desafio.api.viewsets import DesafioViewSet, FemaleViewSet, MaleViewSet


route = routers.DefaultRouter()


route.register(r'desafio', desafioviewsets.DesafioViewSet, basename='Desafio')
route.register(r'm', desafioviewsets.MaleViewSet, basename='Male')
route.register(r'f', desafioviewsets.FemaleViewSet, basename='Female')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    # path('desafio/<str>', ListaMale.as_view()),
    path('upload_excel', views.upload_excel, name='upload_excel'),
    path('read_excel', views.read_excel, name='read_excel'),
]
