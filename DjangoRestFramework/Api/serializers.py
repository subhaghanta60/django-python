from rest_framework import serializers
from .models import Product,Order,OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= ('id','name','description','price','stock')
    

    def validate_price(self, value):
        if value <= 0 :
            raise serializers.ValidationError(
                "Price must be Greater than 0."
            )
        return value

class OrderItemSerializer(serializers.ModelSerializer):
    # product=ProductSerializer()
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(max_digits=10,decimal_places=2,source='product.price')

    class Meta:
        model=OrderItem
        fields=('product_name','product_price','quantity','item_subtotal')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only=True)
    total_price= serializers.SerializerMethodField(method_name='total')

    # def get_total_price(self,obj):
    #     order_items= obj.items.all()
    #     return sum(order_item.item_subtotal for order_item in order_items)
    def total(self,obj):
        order_items= obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)

    class Meta:
        model=Order
        fields=(
            'order_id',
            'user',
            'created_at',
            'status',
            'items',
            'total_price'
            )