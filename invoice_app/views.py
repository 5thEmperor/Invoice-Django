from django.shortcuts import render
from rest_framework import viewsets
from invoice_app.models import Invoice
from invoice_app.serializer import InvoiceSerializer
# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer