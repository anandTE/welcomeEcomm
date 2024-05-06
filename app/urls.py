from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import ItemViewSet, MyCartViewSet, MyOrdersViewSet, OrderViewSet, PaidOrdersAPIView

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='all-items')
router.register(r'my-cart', MyCartViewSet, basename='my-cart')
router.register(r'my-orders', MyOrdersViewSet, basename='my-orders')
router.register(r'orders', OrderViewSet, basename='orders')




urlpatterns = [
    path('', include(router.urls)),
    path('order-detail/<int:user_id>/', PaidOrdersAPIView.as_view(), name='paid-orders'),
]
