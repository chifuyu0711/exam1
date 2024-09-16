from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
