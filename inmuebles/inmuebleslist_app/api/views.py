from rest_framework.response import Response
from inmuebleslist_app.api.serializers import EdificacionSerializer, EmpresaSerializer
from inmuebleslist_app.models import Edificacion, Empresa
#from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.views import APIView

class EmpresaAV(APIView):
    def get(self, request):
        empresas = Empresa.objects.all()
        # many = tru : indica que se returna una coleccion 
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data,  status = status.HTTP_200_OK)

    def post(self, request):
        serializer =  EmpresaSerializer(data= request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class EdificacionAV(APIView):
    def get(self, request):
        inmuebles = Edificacion.objects.all()
        # many = tru : indica que se returna una coleccion 
        serializer = EdificacionSerializer(inmuebles, many=True)
        return Response(serializer.data,  status = status.HTTP_200_OK)

    def post(self, request):
        serializer = EdificacionSerializer(data= request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EdificacionDetalleAV(APIView):

    def get(self, request, pk):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({
                'rrror': 'La edificacion no existe'
                }, status = status.HTTP_404_NOT_FOUND)
        
        serializer = EdificacionSerializer(edificacion)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({
                'rrror': 'La edificacion no existe'
                }, status = status.HTTP_404_NOT_FOUND)
        
        serializer = EdificacionSerializer(edificacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors,  status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({
                'rrror': 'La edificacion no existe'
                }, status = status.HTTP_404_NOT_FOUND)
        
        edificacion.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)






"""
#Devuelve un metodo Get -Post
@api_view(['GET', 'POST'])
def inmueble_list(request):
    if request.method == 'GET':
        inmuebles = Edificacion.objects.all()
        #Devuelve una colleccion 
        serializer = EdificacionSerializer(inmuebles, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        de_serializer = InmuebleSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else: 
            return Response(de_serializer.errors)

#Devuelve un metodo Get    
@api_view(['GET', 'PUT', 'DELETE'])
def inmueble_detalle(request, pk):
    if request.method == 'GET':
        try:
            inmueble = Edificacion.objects.get(pk=pk)
            serializer = InmuebleSerializer(inmueble)
            return Response(serializer.data)
        except Edificacion.DoesNotExist:
            return Response({
                'Error': 'La inmuebles no existe'
                }, status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        inmueble = Edificacion.objects.get(pk=pk)
        de_serializer = InmuebleSerializer(inmueble, data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return Response(de_serializer.errors,  status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            inmueble = Edificacion.objects.get(pk=pk)
            inmueble.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Edificacion.DoesNotExist:
            return Response({
                'Error': 'El inmuebles no existe'
                }, status = status.HTTP_404_NOT_FOUND)
"""