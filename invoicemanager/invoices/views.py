from django.shortcuts import render

from rest_framework import generics
from .models import Customer, Invoice, InvoiceTemplate
from .serializers import CustomerSerializer, InvoiceSerializer, InvoiceTemplateSerializer

class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class InvoiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceTemplateListCreateAPIView(generics.ListCreateAPIView):
    queryset = InvoiceTemplate.objects.all()
    serializer_class = InvoiceTemplateSerializer

class InvoiceTemplateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceTemplate.objects.all()
    serializer_class = InvoiceTemplateSerializer

from .models import InvoiceTemplate
from .utils import generate_invoice_html

def generate_invoice(request):
    # Retrieve selected template (assuming template_id is provided in request data)
    template_id = request.POST.get('template_id')  # Assuming POST request is used
    template = InvoiceTemplate.objects.get(pk=template_id)

    # Generate invoice HTML content using selected template and user input data
    invoice_data = {
        # Populate with relevant data for the invoice
    }
    invoice_html = generate_invoice_html(template.html_content, invoice_data)

    # Further processing (e.g., save to PDF, send email, etc.)
    # ...

    return render(request, 'invoice.html', {'invoice_html': invoice_html})

