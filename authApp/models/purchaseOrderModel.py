from django.db import models
from .userModel import User
from .supplierModel import Supplier
from datetime import datetime

class PurchaseOrder(models.Model):
    id = models.AutoField(primary_key=True)
    createdByUserId = models.ForeignKey(User, related_name='purchaseOrderCreatedByUserId', on_delete=models.CASCADE)
    idSupplier = models.ForeignKey(Supplier, related_name='purchaseOrderIdSupplier', on_delete=models.CASCADE)
    paymentMethod = models.CharField('PaymentMethod', max_length=50, default=0)
    date = models.DateTimeField(default=datetime.now)
    status = models.CharField('Status', max_length=20, default=0)


