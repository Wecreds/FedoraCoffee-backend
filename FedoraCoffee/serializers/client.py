from rest_framework.serializers import ModelSerializer

from FedoraCoffee.models import Client

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"