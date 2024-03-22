from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default = None)
    date = models.DateField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
    # Add other fields as needed

class InvoiceTemplate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    template_name = models.CharField(max_length=100)
    html_content = models.TextField(default = None)

