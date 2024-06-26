from django.urls import path

from invoice.views import (
    create_invoice, create_invoice_item, InvoiceList, InvoiceList, InvoiceDetailView, assess_invoice
    )

urlpatterns = [
    path('create', create_invoice, name='create_invoice'),
    path('index', InvoiceList.as_view() , name='invoice_list'),
    path('details/<int:pk>', InvoiceDetailView.as_view() , name='invoice_details'),
    path('assess/<int:pk>', assess_invoice , name='assess_invoice'),
    path('item/create/<int:pk>', create_invoice_item, name='create_invoice_item'),
]
