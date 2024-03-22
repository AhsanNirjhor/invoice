from django.urls import path
from .views import (
    CustomerListCreateAPIView, CustomerRetrieveUpdateDestroyAPIView,
    InvoiceListCreateAPIView, InvoiceRetrieveUpdateDestroyAPIView,
    InvoiceTemplateListCreateAPIView, InvoiceTemplateRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Customer URLs
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-retrieve-update-destroy'),

    # Invoice URLs
    path('invoices/', InvoiceListCreateAPIView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceRetrieveUpdateDestroyAPIView.as_view(), name='invoice-retrieve-update-destroy'),

    # Invoice Template URLs
    path('invoice-templates/', InvoiceTemplateListCreateAPIView.as_view(), name='invoice-template-list-create'),
    path('invoice-templates/<int:pk>/', InvoiceTemplateRetrieveUpdateDestroyAPIView.as_view(), name='invoice-template-retrieve-update-destroy'),
]
