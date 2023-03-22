from .views import *
from django.urls import path


urlpatterns = [
    path('', InvoiceViewSet.as_view({'get': 'list',
    'post': 'create'}),name='InvoiceView'),

]