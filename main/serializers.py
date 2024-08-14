from rest_framework import serializers
from . import models
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id','user', 'address']
        
        
class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id','user', 'address']
        
        
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id','category', 'vendor','title','detail','price']
        
    def __init__ (self,*args,**kwargs):
        super(ProductListSerializer, self).__init__(*args,**kwargs) 
        self.Meta.depth = 1
        
        


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)
    vendor = serializers.CharField(source='vendor.user.username', read_only=True)

    class Meta:
        model = models.Product
        fields = ['id','category', 'vendor','title','detail','price']
