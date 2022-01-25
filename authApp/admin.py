from django.contrib import admin
from .models.userModel import User
from .models.clientModel import Client
from .models.invoiceModel import Invoice
from .models.productModel import Product
from .models.productInvoiceModel import ProductInvoice
from .models.supplierModel import Supplier
from .models.purchaseOrderModel import PurchaseOrder
from .models.productPurchaseOrderModel import ProductPurchaseOrder

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Invoice)
admin.site.register(Product)
admin.site.register(ProductInvoice)
admin.site.register(Supplier)
admin.site.register(PurchaseOrder)
admin.site.register(ProductPurchaseOrder)

