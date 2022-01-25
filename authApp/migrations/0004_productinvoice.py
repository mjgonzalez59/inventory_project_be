# Generated by Django 3.2.8 on 2021-10-27 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInvoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('unitPrice', models.IntegerField(default=0)),
                ('taxPercentage', models.IntegerField(default=0)),
                ('idInvoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productInvoiceIdInvoice', to='authApp.invoice')),
                ('idProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productInvoiceIdProduct', to='authApp.product')),
            ],
        ),
    ]