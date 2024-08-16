from rest_framework.viewsets import ModelViewSet

from FedoraCoffee.models import Item
from FedoraCoffee.serializers import ItemSerializer

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer