"""projectSCS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authApp import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view()),
    path('user/delete/<int:pk>/', views.UserDeleteView.as_view()),
    path('user/list/', views.UserListView.as_view()),
    path('client/', views.ClientCreateView.as_view()),
    path('client/<int:pk>/', views.ClientDetailView.as_view()),
    path('client/clientByCC/<int:pk>/', views.ClientByCC.as_view()),
    path('client/update/<int:pk>/', views.ClientUpdateView.as_view()),
    path('client/delete/<int:pk>/', views.ClientDeleteView.as_view()),
    path('client/list/', views.ClientListView.as_view()),
    path('invoice/', views.InvoiceCreateView.as_view()),
    path('invoice/<int:pk>/', views.InvoiceDetailView.as_view()),
    path('invoice/update/<int:pk>/', views.InvoiceUpdateView.as_view()),
    path('invoice/delete/<int:pk>/', views.InvoiceDeleteView.as_view()),
    path('invoice/list/', views.InvoiceListView.as_view()),
    path('product/', views.ProductCreateView.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view()),
    path('product/productByName/<str:pk>/', views.ProductByName.as_view()),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view()),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view()),
    path('product/list/', views.ProductListView.as_view()),
    # path('productInvoice/', views.ProductInvoiceCreateView.as_view()),
    # path('productInvoice/<int:pk>/', views.ProductInvoiceDetailView.as_view()),
    # path('productInvoice/update/<int:pk>/', views.ProductInvoiceUpdateView.as_view()),
    path('productPurchaseOrder/', views.ProductPurchaseOrderCreateView.as_view()),
    path('productPurchaseOrder/<int:pk>/', views.ProductPurchaseOrderDetailView.as_view()),
    path('productPurchaseOrder/update/<int:pk>/', views.ProductPurchaseOrderUpdateView.as_view()),
    path('supplier/', views.SupplierCreateView.as_view()),
    path('supplier/<int:pk>/', views.SupplierDetailView.as_view()),
    path('supplier/update/<int:pk>/', views.SupplierUpdateView.as_view()),
    path('supplier/delete/<int:pk>/', views.SupplierDeleteView.as_view()),
    path('supplier/list/', views.SupplierListView.as_view()),
    path('supplier/supplierBycompanyId/<int:pk>/', views.SupplierBycompanyId.as_view()),
    path('purchaseOrder/', views.PurchaseOrderCreateView.as_view()),
    path('purchaseOrder/<int:pk>/', views.PurchaseOrderDetailView.as_view()),
    path('purchaseOrder/update/<int:pk>/', views.PurchaseOrderUpdateView.as_view()),
    path('purchaseOrder/delete/<int:pk>/', views.PurchaseOrderDeleteView.as_view()),
    path('purchaseOrder/list/', views.PurchaseOrderListView.as_view())
]


