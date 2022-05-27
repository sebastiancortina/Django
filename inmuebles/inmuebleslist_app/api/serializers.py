from turtle import mode
from rest_framework import serializers
from inmuebleslist_app.models import Edificacion, Empresa, Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    comentario_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comentario
        exclude = ['edificacion']
        #fields = "__all__"


class EdificacionSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    class Meta:
        model = Edificacion
        fields = "__all__"
        #fields = ['id','pais','active','image']
        #exclude = ['id']

class EmpresaSerializer(serializers.ModelSerializer):
    #edificacionlist = serializers.StringRelatedField(many=True, read_only=True)
    edificacionlist = EdificacionSerializer(many=True, read_only=True)
    #edificacionlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #edificacionlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """edificacionlist = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True,
        view_name='edificacion-detalle',
        )
    """
    class Meta:
        model = Empresa
        fields = "__all__"
    

#permite hacer un mapeo de todo la clase entidad

















    """
    def get_longitud_direccion(self, object):
        cantidad_caracteres = len(object.direccion)
        return cantidad_caracteres

    def validate(self, data):
        if data['direccion'] == data['pais']:
            raise serializers.ValidationError("La direccion y el pais deben ser difernetes")
        else:
            return data
    
    def validate_image(self,data):
        if len(data) < 2:
            raise serializers.ValidationError("La Url de la imagen es muy corta")
        else:
            return data 
    """




















#validacion personalizada 
"""
def column_longitud(value):
    if len(value) < 2:
        raise serializers.ValidationError("La direccion es demasiado corta")

class InmuebleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    direccion = serializers.CharField(validators = [column_longitud])
    pais = serializers.CharField(validators = [column_longitud])
    descripcion = serializers.CharField()
    image = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Inmueble.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.pais = validated_data.get('pais', instance.pais)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.image = validated_data.get('image', instance.image)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        
        return instance
    
    def validate(self, data):
        if data['direccion'] == data['pais']:
            raise serializers.ValidationError("La direccion y el pais deben ser difernetes")
        else:
            return data
    
    def validate_image(self,data):
        if len(data) < 2:
            raise serializers.ValidationError("La Url de la imagen es muy corta")
        else:
            return data 
"""