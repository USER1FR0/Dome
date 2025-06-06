from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.helloworld),
    path('login/', views.iniciarSesion),
    path('logout/', views.cerrarSesion),
    path('registro/', views.registro),
    path('dispositivos/', views.dispositivos),
    path('dashboard/', views.dashboard),
    path('datos-tiempo-real/', views.datos_tiempo_real, name="tiempo"),
    # Agrega estas rutas:
    path('dispositivos/agregar/', views.agregar_dispositivo, name='agregar_dispositivo'),
    path('dispositivos/editar/<int:dispositivo_id>/', views.editar_dispositivo, name='editar_dispositivo'),
    path('dispositivos/eliminar/<int:dispositivo_id>/', views.eliminar_dispositivo, name='eliminar_dispositivo'),
    path('control/', views.lista_registros, name='control'),

]