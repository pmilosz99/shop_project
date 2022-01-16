from django.urls import path, include
from rest_framework import routers

from my_shop.shop.views import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('shop/', include(router.urls)),
]