from django.contrib import admin
from django.urls import path
#from inmuebleslist_app.api.views import inmueble_list, inmueble_detalle
from inmuebleslist_app.api.views import InmuebleListAV, InmuebleDetalle
urlpatterns = [
    path('list/', InmuebleListAV.as_view(), name='inmueble-list'),
    path('<int:pk>', InmuebleDetalle.as_view(), name='inmueble-detalle')
]