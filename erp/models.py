from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Product(models.Model):
    productcategory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    cost = models.FloatField()
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Employee(models.Model):
    name = models.CharField(max_length=255, unique=True)
    age = models.PositiveIntegerField()
    salary = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Costumer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    age = models.PositiveIntegerField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PaymentMethod(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Sale(models.Model):
    costumer = models.ForeignKey(Costumer, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    paymentmethod = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SaleItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    quantity = models.FloatField()
