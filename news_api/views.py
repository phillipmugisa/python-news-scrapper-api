from unicodedata import category
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import NewsSerializer
from .models import NewsArticle
from rest_framework import pagination, response
from rest_framework import filters
from rest_framework.views import View
from django.db.models import Q
from django.http import HttpResponse

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

class CustomSearchFilter(filters.SearchFilter):
    def filter_queryset(self, request, queryset, view):
        if request.GET.get('category', None) and not request.GET.get('source', None):
            return queryset.filter(category = request.GET.get('category').lower())
        elif not request.GET.get('category', None) and request.GET.get('source', None):
            return queryset.filter(source__name = request.GET.get('source'))
        elif request.GET.get('category', None) and request.GET.get('source', None):
            return queryset.filter(Q(category = request.GET.get('category').lower()) & Q(source__name = request.GET.get('source')))
        return super().filter_queryset(request, queryset, view)

class NewsListView(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
    filter_backends = [CustomSearchFilter]
    # filterset_fields = ['category', 'source__name']