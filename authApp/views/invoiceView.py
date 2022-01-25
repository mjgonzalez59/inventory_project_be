from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings
from datetime import datetime
from django.core import serializers
import json

from authApp.models.invoiceModel import Invoice
from authApp.models.productModel import Product
from authApp.serializers.invoiceSerializer import InvoiceSerializer
from authApp.serializers.productInvoiceSerializer import ProductInvoiceSerializer
from authApp.otherEquations.myEquations import calculateSubTotal, calculateValueWithTax

class InvoiceCreateView(generics.CreateAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        invoiceData = {
            "createdByUserId": valid_data['user_id'], 
            "idClient": request.data['idClient'], 
            "paymentMethod": request.data['paymentMethod'], 
            "date": datetime.now(), 
            "status": "Pending"
        }
 
        serializer = InvoiceSerializer(data=invoiceData)
        serializer.is_valid(raise_exception=True)
        invoiceInstance = serializer.save()
        invoiceId = invoiceInstance.id

        productList = []

        productsListInput = request.data['products']
        for product in productsListInput:
            productQueryObject = Product.objects.get(id=product['idProduct'])
            unitPrice = productQueryObject.sellPrice
            quantity = product['quantity']
            taxPercentage = product['taxPercentage']

            subTotalValue = calculateSubTotal(quantity, unitPrice)
            valueWithTax = calculateValueWithTax(subTotalValue, taxPercentage)

            ProductInvoiceData = {
                "idInvoice": invoiceId,
                "idProduct": product['idProduct'],
                "quantity": quantity,
                "unitPrice": unitPrice,
                "taxPercentage": taxPercentage,
                "subtotal" : subTotalValue,
                "total" : valueWithTax
            }
            #ProductList is being added with each product
            productList.append(ProductInvoiceData)

            #Is being created ProductInvoice (many to many table between product and invoice) for each product from the request.data
            serializer = ProductInvoiceSerializer(data=ProductInvoiceData)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        Invoice.objects.filter(id=invoiceId).update(status='Active')
        invoiceUpdated = Invoice.objects.get(id=invoiceId)


        responseData = {
            "id": invoiceId,
            "idClient": invoiceUpdated.id,
            "paymentMethod": invoiceUpdated.paymentMethod, 
            "date": invoiceUpdated.date, 
            "status": invoiceUpdated.status,
            "products": productList
        }

        # return Response("Invoice creado", status=status.HTTP_201_CREATED)
        return Response(responseData, status=status.HTTP_201_CREATED)




class InvoiceDetailView(generics.RetrieveAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Invoice.objects.filter(status="Active")

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)




class InvoiceUpdateView(generics.UpdateAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Invoice.objects.all()

    def post(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)



class InvoiceDeleteView(generics.DestroyAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Invoice.objects.all()

    def get(self, request, *args, **kwargs):
        Invoice.objects.filter(id=kwargs['pk']).update(status='Inactive')
        return Response("Invoice eliminada", status=status.HTTP_201_CREATED)



class InvoiceListView(generics.ListAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Invoice.objects.filter(status='Active')
        return queryset




            # productQuerySetObject = Product.objects.filter(id=product['idProduct'])
            # productJSONObject = serializers.serialize("json", productQuerySetObject)
            # productObject = json.loads(productJSONObject)           

            # for item in productObject: 
            #     productFields = item['fields']
            #     productSellPrice = productFields['sellPrice']

            # unitPrice = productSellPrice