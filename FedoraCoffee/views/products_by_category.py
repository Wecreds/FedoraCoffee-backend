from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from FedoraCoffee.models import Product, Category
from FedoraCoffee.serializers import CustomProductSerializer 

class ProductsByCategoryView(APIView):
    def get(self, request):
        category_id = request.GET.get("category", 1)
        page = int(request.GET.get("page", 1))
        # page_size = 10
        
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({"error": "Category does not exist."}, status=status.HTTP_404_NOT_FOUND)

        products = Product.objects.filter(category=category)

        start = (page - 1) * 10
        end = start + 10
        paginated_products = products[start:end]

        serializer = CustomProductSerializer(paginated_products, many=True)

        total_pages = (products.count() + 10 - 1) // 10

        return Response({
            "total_pages": total_pages,
            "products": serializer.data
        }, status=status.HTTP_200_OK)