from rest_framework import serializers
from authApp.models.invoiceModel import Invoice
from authApp.models.userModel import User
from authApp.models.clientModel import Client
from authApp.models.productInvoiceModel import ProductInvoice
from authApp.otherEquations.myEquations import calculateSubTotal, calculateValueWithTax


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ["createdByUserId", "idClient", "paymentMethod", "date", "status"]

    def to_representation(self, obj):
        invoiceRepresentation = Invoice.objects.get(id=obj.id)
        userRepresentation = User.objects.get(id=obj.createdByUserId.id)
        clientRepresentation = Client.objects.get(id=obj.idClient.id)
        productInvoiceRepresentation = ProductInvoice.objects.filter(idInvoice_id=obj.id)
        totalValue = 0
        products = []

        for elem in productInvoiceRepresentation:
            product = {}
            product["id"] = elem.idProduct.id
            product["name"] = elem.idProduct.name
            product["quantity"] = elem.quantity
            product["unitPrice"] = elem.unitPrice
            product["taxPercentage"] = elem.taxPercentage
            subTotalValue = calculateSubTotal(elem.quantity, elem.unitPrice)
            valueWithTax = calculateValueWithTax(subTotalValue, elem.taxPercentage)
            totalValue += valueWithTax
            product["subTotalValue"]= subTotalValue
            product["valueWithTax"]= valueWithTax
            products.append(product)

        return {
            "id": invoiceRepresentation.id,
            "createdByUser": userRepresentation.username, 
            "idClient": {
                "cc": clientRepresentation.cc,
                "id": clientRepresentation.id,
                "name": clientRepresentation.name,
                "address": clientRepresentation.address,
                "phone": clientRepresentation.phone,
                "email": clientRepresentation.email,
                "country": clientRepresentation.country,
                "contactName": clientRepresentation.contactName,
                "status": clientRepresentation.status,
            }, 
            "paymentMethod": invoiceRepresentation.paymentMethod, 
            "date": invoiceRepresentation.date, 
            "products": products,
            "totalValue": totalValue,
            "status": invoiceRepresentation.status
        }

