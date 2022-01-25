from rest_framework import serializers
from authApp.models.productInvoiceModel import ProductInvoice
from authApp.models.invoiceModel import Invoice
from authApp.models.productModel import Product

class ProductInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInvoice
        fields = ["idInvoice", "idProduct", "quantity", "unitPrice", "taxPercentage"]


    def to_representation(self, obj):
        productInvoiceRepresentation = ProductInvoice.objects.get(id=obj.id)
        invoiceRepresentation = Invoice.objects.get(id=obj.id)
        productRepresentation = Product.objects.get(id=obj.id)

        return {
            "id": productInvoiceRepresentation.id,
            "idInvoice": invoiceRepresentation.id, 
            "idProduct": productRepresentation.id, 
            "quantity": productInvoiceRepresentation.quantity, 
            "unitPrice": productInvoiceRepresentation.unitPrice, 
            "taxPercentage": productInvoiceRepresentation.taxPercentage
        }


