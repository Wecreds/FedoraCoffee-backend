from rest_framework.serializers import ModelSerializer

from FedoraCoffee.models import Order_product

class orderProductSerializer(ModelSerializer):
    class Meta:
        model = Order_product
        fields = "__all__"