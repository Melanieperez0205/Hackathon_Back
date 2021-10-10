from authAppExample.models.clase import Clase
from rest_framework             import serializers

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Clase
        fields = ['id', 'temaclase','descripcionclase']