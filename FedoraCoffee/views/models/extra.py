from rest_framework.viewsets import ModelViewSet

from FedoraCoffee.models import Extra
from FedoraCoffee.serializers import ExtraSerializer

class ExtraViewSet(ModelViewSet):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer