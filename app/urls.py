from django.urls import path
from .views import CustomerLoginAPIView, CustomerTokenObtainPairView

urlpatterns = [
    path('login/', CustomerLoginAPIView.as_view(), name='customer_login'),
    path('token/', CustomerTokenObtainPairView.as_view(), name='customer_token_obtain_pair'),
]
