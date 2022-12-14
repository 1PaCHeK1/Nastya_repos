from pyexpat import model
from rest_framework.serializers import ModelSerializer, Serializer

from .models import (
    User
)

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
