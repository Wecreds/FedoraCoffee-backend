from rest_framework.viewsets import ModelViewSet

from FedoraCoffee.models import Order_extra
from FedoraCoffee.serializers import orderExtraSerializer

class orderExtraViewSet(ModelViewSet):
    queryset = Order_extra.objects.all()
    serializer_class = orderExtraSerializer