from rest_framework.serializers import ModelSerializer

from FedoraCoffee.models import orderExtra

class orderExtraSerializer(ModelSerializer):
    class Meta:
        model = orderExtra
        fields = "__all__"