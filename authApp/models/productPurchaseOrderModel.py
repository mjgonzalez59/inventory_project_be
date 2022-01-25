from django.db import models
from .purchaseOrderModel import PurchaseOrder
from .productModel import Product

class ProductPurchaseOrder(models.Model):
    id = models.AutoField(primary_key=True)
    idPurchaseOrder = models.ForeignKey(PurchaseOrder, related_name='productPurchaseOrderIdPurchaseOrder', on_delete=models.CASCADE)
    idProduct = models.ForeignKey(Product, related_name='productPurchaseOrderIdProduct', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    unitPrice = models.FloatField(default=0)
    taxPercentage = models.FloatField(default=0)


