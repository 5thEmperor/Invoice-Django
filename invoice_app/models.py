from django.db import models

class Invoice(models.Model):
    date = models.DateField()
    invoice_no = models.CharField(max_length=50)
    customername = models.CharField(max_length=100)   

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_details')
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=15, decimal_places=4)
    price = models.DecimalField(max_digits=15, decimal_places=4)