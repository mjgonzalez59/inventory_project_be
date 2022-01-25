from django.db import models
from .userModel import User
from .clientModel import Client
from datetime import datetime

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    createdByUserId = models.ForeignKey(User, related_name='invoiceCreatedByUserId', on_delete=models.CASCADE)
    idClient = models.ForeignKey(Client, related_name='invoiceIdClient', on_delete=models.CASCADE)
    paymentMethod = models.CharField('PaymentMethod', max_length=50, default=0)
    date = models.DateTimeField(default=datetime.now)
    status = models.CharField('Status', max_length=20, default=0)


