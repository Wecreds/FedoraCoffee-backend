from rest_framework.serializers import ModelSerializer

from FedoraCoffee.models import Order

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"