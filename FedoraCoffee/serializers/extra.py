from rest_framework.serializers import ModelSerializer

from FedoraCoffee.models import Extra

class ExtraSerializer(ModelSerializer):
    class Meta:
        model = Extra
        fields = "__all__"