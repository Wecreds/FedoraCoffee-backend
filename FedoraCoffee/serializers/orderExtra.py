from rest_framework.serializers import ModelSerializer

from FedoraCoffee.models import Order_extra

class orderExtraSerializer(ModelSerializer):
    class Meta:
        model = Order_extra
        fields = "__all__"