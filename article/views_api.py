from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from article.serializers import ArticleSerializer
from article.models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
