from rest_framework.serializers import ModelSerializer

from FedoraCoffee.models import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        verbose_name_plural = "categories"

        