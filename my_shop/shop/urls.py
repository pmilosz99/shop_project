from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, ProductViewSet, product_list ,product_detail

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('api/shop/', include(router.urls)),
    path('', product_list, name='product_list'),
    path('<category_slug>/', product_list, name='product_list_by_category'),
    path('<id>/<slug>/', product_detail, name='product_detail')
]
