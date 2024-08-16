from rest_framework.viewsets import ModelViewSet

from FedoraCoffee.models import Category
from FedoraCoffee.serializers import CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer