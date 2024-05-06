from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Item, OrderItem, Order
from .serializers import ItemSerializer, CartItemSerializer, OrderSerializer
from rest_framework.views import APIView

from rest_framework.response import Response

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]  # No authentication required


class MyCartViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    queryset = OrderItem.objects.all()  # Necessary for DRF, but will be overridden
    def get_queryset(self):
        user = self.request.user
        return OrderItem.objects.filter(order__user=user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset().first()  # Assuming only one cart per user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
class MyOrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)
    




class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, serializer):
        data = self.request.data
        items = data['items']
        total_amount = 0
        if items:
            for x in items:
                qs = Item.objects.filter(id=x)
                if qs:
                    total_amount += qs.last().price
        

        order = Order.objects.create(
            user=self.request.user, total_amount=total_amount
        )
        order.items.set(items)
        order.save()

        return Response(self.serializer_class(order).data)


    def update(self, request, *args, **kwargs):
        import pdb;pdb.set_trace()
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        items = request.data.get('items', [])
        total_amount = 0
        if items:
            for item_id in items:
                qs = Item.objects.filter(id=item_id)
                if qs.exists():
                    total_amount += qs.last().price

        instance.total_amount = total_amount
        instance.save()
        self.perform_update(serializer)

        return Response(serializer.data)


class PaidOrdersAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, ):
        paid_orders = Order.objects.filter(user=request.user, is_paid=True)
        serializer = OrderSerializer(paid_orders, many=True)
        return Response(serializer.data)
class MyKartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        unpaid_orders = Order.objects.filter(user=request.user, is_paid=False)
        serializer = OrderSerializer(unpaid_orders, many=True)
        return Response(serializer.data)