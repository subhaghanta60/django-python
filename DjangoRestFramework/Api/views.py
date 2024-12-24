from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from Api.serializers import ProductSerializer,OrderSerializer,ProductInfoSerializer
from Api.models import Product, Order

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Max

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny
)

from rest_framework.views import APIView

from Api.filters import ProductFilter

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ProductListAPIView(generics.ListAPIView):

    queryset = Product.objects.filter(stock__gt=0)
    serializer_class = ProductSerializer
   

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'



class OrderListAPIView(generics.ListAPIView):

    queryset = Order.objects.prefetch_related('items','items__product').all()
    serializer_class = OrderSerializer



class UserOrderListAPIView(generics.ListAPIView):

    queryset = Order.objects.prefetch_related('items','items__product').all()
    serializer_class = OrderSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs= super().get_queryset()
        return qs.filter(user= user)


class ProductCreateAPIView(generics.CreateAPIView):
    model=Product
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filterset_fields = ('name','price')
    filterset_class= ProductFilter
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
        ]
    search_fields = ['=name','description']
    ordering_fields =['name','price','stock']

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()



class ProductDetailUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

# @api_view(['GET'])
# def product_list(request):
#     products=Product.objects.all()
#     serializer = ProductSerializer(products, many=True)

    # return JsonResponse({
    #     'data': serializer.data
    # })
    # return Response(serializer.data)


# @api_view(['GET'])
# def product_details(request,pk):

#     product=get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)




# @api_view(['GET'])
# def order_list(request):
#     order=Order.objects.all()
#     serializer = OrderSerializer(order, many=True)

#     return Response(serializer.data)

#optimize Queries

# @api_view(['GET'])
# def order_list(request):
#     #order=Order.objects.prefetch_related('items','items__product').all()
#     order=Order.objects.prefetch_related('items__product').all()
#     serializer = OrderSerializer(order, many=True)

#     return Response(serializer.data)


class ProductInfoAPIView(APIView):
    def get(self, request):
        products= Product.objects.all()
        serializer = ProductInfoSerializer({
        'products':products,
        'count': len(products),
        'max_price':products.aggregate(max_price=Max('price'))['max_price']
         })
        return Response(serializer.data)



# @api_view(['GET'])
# def product_info(request):
#     products= Product.objects.all()
#     serializer = ProductInfoSerializer({
#         'products':products,
#         'count': len(products),
#         'max_price':products.aggregate(max_price=Max('price'))['max_price']

#     })
#     return Response(serializer.data)



