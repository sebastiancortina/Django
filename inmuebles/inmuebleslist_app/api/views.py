from matplotlib.style import context
from rest_framework.response import Response
from inmuebleslist_app.api.serializers import EdificacionSerializer, EmpresaSerializer, ComentarioSerializer
from inmuebleslist_app.models import Edificacion, Empresa, Comentario
#from rest_framework.decorators import api_view 
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

class ComentarioCreate(generics.CreateAPIView):
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        return Comentario.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        inmueble = Edificacion.objects.get(pk=pk)

        # Captura el usuario que crea el comentario 
        user = self.request.user
        comentario_queryset = Comentario.objects.filter(edificacion= inmueble, comentario_user = user)

        if comentario_queryset.exists():
            raise ValidationError('El usuario ya escribir un comentario para este inmueble')

        serializer.save(edificacion=inmueble, comentario_user=user)

class ComentarioList(generics.ListCreateAPIView):
    #queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comentario.objects.filter(edificacion=pk)

class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer



"""
class ComentarioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ComentarioDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
"""    
class EmpresaVS(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer




"""
class EmpresaVS(viewsets.ViewSet):
    def list(self, request):
        queryset = Empresa.objects.all()
        serializer = EmpresaSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Empresa.objects.all()
        edificacionlist = get_object_or_404(queryset, pk=pk)
        serializer = EmpresaSerializer(edificacionlist)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'empresa no encontrada'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = EmpresaSerializer(empresa, data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'empresa no encontrada'}, status=status.HTTP_400_BAD_REQUEST)
        
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
class EmpresaAV(APIView):
    def get(self, request):
        empresas = Empresa.objects.all()
        # many = tru : indica que se returna una coleccion 
        serializer = EmpresaSerializer(empresas, many=True, context={'request': request})
        return Response(serializer.data,  status = status.HTTP_200_OK)

    def post(self, request):
        serializer =  EmpresaSerializer(data= request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class EmpresaDetalleAV(APIView):
    def get(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'},status.HTTP_404_NOT_FOUND)    

        serializer = EmpresaSerializer(empresa, context={'request': request})
    
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encotrada'}, status.HTTP_404_NOT_FOUND)
        
        serializer = EmpresaSerializer(empresa, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encotrada'}, status.HTTP_404_NOT_FOUND)
        
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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