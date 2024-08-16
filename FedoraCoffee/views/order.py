from rest_framework.viewsets import ModelViewSet

from FedoraCoffee.models import Order
from FedoraCoffee.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer