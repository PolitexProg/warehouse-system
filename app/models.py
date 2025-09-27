# models.py
from django.db import models
from rest_framework.exceptions import ValidationError
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=6, unique=True)

class Material(models.Model):
    material_name = models.CharField(max_length=100)

class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.PositiveIntegerField()