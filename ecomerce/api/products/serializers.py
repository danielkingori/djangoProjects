from rest_framework.serializers import ModelSerializer
from products.models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "created_by"]
        
        
#testing
#auth & permissions
#ordering & filtering
#docs, pagination, cache, throtling, groups
