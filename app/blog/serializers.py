from pyexpat import model
from rest_framework.serializers import ModelSerializer, Serializer

from .models import (
    Comment
)

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['article', 'text', 'creator']
        read_only = '__all__'