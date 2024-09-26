from rest_framework import viewsets, generics
from .serializers import ProductSerializer
from products.models import Product
from rest_framework.permissions import IsAuthenticated
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    
    # """
    # {
    #     "Authorization":"Bearer  ddddddddddddd"
    # }
    # """