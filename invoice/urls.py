from django.urls import path

from invoice.views import (
    create_invoice, create_invoice_item, InvoiceList, InvoiceList
    )

urlpatterns = [
    path('create', create_invoice, name='create_invoice'),
    path('index', InvoiceList.as_view() , name='invoice_list'),
    path('item/create/<int:pk>', create_invoice_item, name='create_invoice_item'),
]
