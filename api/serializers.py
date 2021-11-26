from rest_framework.serializers import ModelSerializer
from .models import Nota


class NotaSerializer(ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'
