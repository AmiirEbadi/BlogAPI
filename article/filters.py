from dataclasses import field
import django_filters
from .models import Article

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title' , lookup_expr='iexact')

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Article
        fields = [
            'is_special'
        ]
        