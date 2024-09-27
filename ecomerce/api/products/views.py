from rest_framework import viewsets, generics
from .serializers import ProductSerializer
from products.models import Product
from rest_framework.permissions import IsAuthenticated
from users.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    # queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
    def get_queryset(self):
        return Product.objects.all()
        return Product.objects.filter(created_by=self.request.user)

@api_view(['GET']) 
def products_list(request):
    return Response({"message":"Hello"})
    #will be useful when we want to do specific changes
    
    # """
    # {
    #     "Authorization":"Bearer  ddddddddddddd"
    # }
    # """
    
    
    # Product.objects.create(name="Product", price=200, created_by=1, description='one')
    # Assuming you have imported your Product model

# Create 100 records using a Python dictionary
# products_data = [
#     {
#         "name": f"Product {i}",
#         "price": 200 + i,  # Varying the price slightly for each product
#         "created_by": User.objects.get(email="dan@gmail.com"),   # Assuming '1' is the ID of the user creating the products
#         "description": f"Description for Product {i}",
#     }
#     for i in range(1, 301)  # Creating 100 records
# ]

# # Inserting the records into the database using a loop
# for product_data in products_data:
#     Product.objects.create(**product_data)

# print("100 products have been created.")
