from urllib import request
from .models import Comment
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect, JsonResponse
 
from django.contrib.auth.decorators import login_required

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin    
)
from .serializers import CommentSerializer, CommentCreateSerializer

from app.utils import header_context
from blog.models import Article


class BlogListView(ListView):
    template_name = 'blog/index.html'
    model = Article
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(header_context(self.request))
        return context


class ArticleDetailView(DetailView):
    template_name = 'blog/blog.html'
    model = Article
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(header_context(self.request))
        context.update({'comments': Comment.objects.filter(article=context['article'])})
        return context


class CommentsJSONView(RetrieveModelMixin,
                    ListModelMixin,
                    CreateModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    GenericViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    
        
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return CommentCreateSerializer
        else:
            return CommentSerializer