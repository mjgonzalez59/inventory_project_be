from re import M
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings
from datetime import datetime
from django.core import serializers
import json

from authApp.models.purchaseOrderModel import PurchaseOrder
from authApp.models.productModel import Product
from authApp.serializers.purchaseOrderSerializer import PurchaseOrderSerializer
from authApp.serializers.productPurchaseOrderSerializer import ProductPurchaseOrderSerializer
from authApp.otherEquations.myEquations import calculateSubTotal, calculateValueWithTax

class PurchaseOrderCreateView(generics.CreateAPIView):
    serializer_class = PurchaseOrderSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        purchaseOrderData = {
            "createdByUserId": valid_data['user_id'], 
            "idSupplier": request.data['idSupplier'], 
            "paymentMethod": request.data['paymentMethod'], 
            "date": datetime.now(), 
            "status": "Pending"
        }

        productList = []

        serializer = PurchaseOrderSerializer(data=purchaseOrderData)
        serializer.is_valid(raise_exception=True)
        purchaseOrderInstance = serializer.save()
        purchaseOrderId = purchaseOrderInstance.id


        productsListInput = request.data['products']
        for eachProduct in productsListInput:

            quantity = eachProduct['quantity']
            taxPercentage = eachProduct['taxPercentage']

            unitPrice = eachProduct['unitPrice']
            subTotalValue = calculateSubTotal(quantity, unitPrice)
            valueWithTax = calculateValueWithTax(subTotalValue, taxPercentage)

            ProductPurchaseOrderData = {
                "idPurchaseOrder": purchaseOrderId,
                "idProduct": eachProduct['idProduct'],
                "quantity": quantity,
                "unitPrice": unitPrice,
                "taxPercentage": taxPercentage,
                "subtotal" : subTotalValue,
                "total" : valueWithTax
            }
            #ProductList is being added with each product
            productList.append(ProductPurchaseOrderData)

            #Here is being created ProductPurchaseOrdere (many to many table between product and PurchaseOrder) for each product from the request.data
            serializer = ProductPurchaseOrderSerializer(data=ProductPurchaseOrderData)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        PurchaseOrder.objects.filter(id=purchaseOrderId).update(status='Active')


        responseData = {
            "idSupplier": purchaseOrderData['idSupplier'], 
            "createdByUserId": purchaseOrderData['createdByUserId'], 
            "paymentMethod": purchaseOrderData['paymentMethod'], 
            "date": purchaseOrderData['date'], 
            "status": purchaseOrderData['status'],
            "products": productList
        }


        return Response(responseData, status=status.HTTP_201_CREATED)




class ProductPurchaseOrderCreateView(generics.CreateAPIView):
    serializer_class = ProductPurchaseOrderSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = ProductPurchaseOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("ProductPurchaseOrder Creada", status=status.HTTP_201_CREATED)










class PurchaseOrderDetailView(generics.RetrieveAPIView):
    serializer_class = PurchaseOrderSerializer
    permission_classes = (IsAuthenticated, )
    queryset = PurchaseOrder.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)




class PurchaseOrderUpdateView(generics.UpdateAPIView):
    serializer_class = PurchaseOrderSerializer
    permission_classes = (IsAuthenticated, )
    queryset = PurchaseOrder.objects.all()

    def post(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)




class PurchaseOrderDeleteView(generics.DestroyAPIView):
    serializer_class = PurchaseOrderSerializer
    permission_classes = (IsAuthenticated, )
    queryset = PurchaseOrder.objects.all()

    def get(self, request, *args, **kwargs):
        PurchaseOrder.objects.filter(id=kwargs['pk']).update(status='updating')
        return Response("Purchase Order eliminada", status=status.HTTP_201_CREATED)



class PurchaseOrderListView(generics.ListAPIView):
    serializer_class = PurchaseOrderSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()
        return queryset
