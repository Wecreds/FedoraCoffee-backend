from rest_framework.viewsets import ModelViewSet

from FedoraCoffee.models import orderExtra
from FedoraCoffee.serializers import orderExtraSerializer

class orderExtraViewSet(ModelViewSet):
    queryset = orderExtra.objects.all()
    serializer_class = orderExtraSerializer