# Generated by Django 5.0.4 on 2024-04-23 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_remove_invoice_quantity_remove_invoice_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
