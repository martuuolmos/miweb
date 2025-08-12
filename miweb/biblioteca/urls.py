from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'), # URL raíz para la aplicación biblioteca
path('pagina1/', views.pagina1, name='pagina1'), # URL para una vista de libros
path('pagina2/', views.pagina2, name='pagina2'), # URL con parámetro
]