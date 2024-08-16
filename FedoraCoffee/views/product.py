from rest_framework.viewsets import ModelViewSet

from FedoraCoffee.models import Product
from FedoraCoffee.serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer