from rest_framework.viewsets import ModelViewSet

from FedoraCoffee.models import Order_product
from FedoraCoffee.serializers import orderProductSerializer

class orderProductViewSet(ModelViewSet):
    queryset = Order_product.objects.all()
    serializer_class = orderProductSerializer