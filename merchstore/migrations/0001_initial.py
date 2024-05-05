# Generated by Django 5.0.2 on 2024-05-03 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('stock', models.IntegerField()),
                ('product_status', models.CharField(choices=[('AVAILABLE', 'Available'), ('OUT OF STOCK', 'Out of Stock'), ('ON SALE', 'On Sale')], default='AVAILABLE', max_length=12)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='user_management.profile')),
                ('Product_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type', to='merchstore.producttype')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
