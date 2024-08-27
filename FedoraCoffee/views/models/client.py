from rest_framework.viewsets import ModelViewSet

from FedoraCoffee.models import Client
from FedoraCoffee.serializers import ClientSerializer

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer