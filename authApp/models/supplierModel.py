from django.db import models

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=50, default=0)
    companyId = models.CharField('CompanyId', max_length=50, default=0)
    address = models.CharField('Address', max_length=50, default=0)
    phone = models.CharField('Phone', max_length=20, default=0)
    email = models.EmailField('Email', max_length=100)
    country = models.CharField('Country', max_length=20, default=0)
    contactName = models.CharField('ConactName', max_length=50, default=0)
    status = models.CharField('Status', max_length=20, default=0)


