from authAppExample.models.comunidad import Comunidad
from rest_framework             import serializers

class ComunidadSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Comunidad
        fields = ['id', 'tipocomunidad', 'register_date','descrpcion']