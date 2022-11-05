
from rest_framework.serializers import ModelSerializer, Serializer, JSONField, ListSerializer, CharField
from django.db.models import QuerySet

from .models import (
    Comment
)


class CommentListSerializer(ListSerializer):
    def to_representation(self, data:QuerySet[Comment]):
        root_comments = data.filter(parent_comment=None)
        comments_dict = {}
        for comment in data:
            if comment.parent_comment:
                (comments_dict
                .setdefault(comment.parent_comment.id, [])
                .append(comment))
        
        result = []
        for root_comment in root_comments:
            result.append(self.push_next_node(comments_dict, root_comment))

        return result

    def push_next_node(self, comments, node):
        data = CommentSerializer(node).data
        if node.id in comments:
            data["children"] = []
            for child in comments[node.id]:
                data["children"].append(self.push_next_node(comments, child))
        return data


class CommentSerializer(ModelSerializer):
    article_name = CharField(source="article.title")
    children = JSONField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "creator",
            "article",
            "article_name",
            "text",
            "created_at",
            "children",
        ]

        extra_kwargs = {
            "children": {"read_only": True}
        }
        list_serializer_class = CommentListSerializer


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['article', 'text', 'creator']
