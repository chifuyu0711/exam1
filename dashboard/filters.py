import django_filters
from django.contrib.auth.models import User
from .models import Category, Product


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = []


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['name']


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = django_filters.CharFilter('category__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'category']
