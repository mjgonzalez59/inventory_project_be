from django.db import models
from .invoiceModel import Invoice
from .productModel import Product

class ProductInvoice(models.Model):
    id = models.AutoField(primary_key=True)
    idInvoice = models.ForeignKey(Invoice, related_name='productInvoiceIdInvoice', on_delete=models.CASCADE)
    idProduct = models.ForeignKey(Product, related_name='productInvoiceIdProduct', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    unitPrice = models.FloatField(default=0)
    taxPercentage = models.FloatField(default=0)


