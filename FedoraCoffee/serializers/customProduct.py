from rest_framework.serializers import ModelSerializer, SlugRelatedField

from FedoraCoffee.models import Product

from uploader.models import Image
from uploader.serializers import ImageSerializer

class CustomProductSerializer(ModelSerializer):
    photo_attachment_key = SlugRelatedField(
        source="photo",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'photo_attachment_key', 'capa', 'photo', 'price']