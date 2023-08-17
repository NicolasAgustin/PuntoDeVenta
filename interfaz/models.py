from django.db import models

# TODO: agregar encriptacion para password

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(default=None)

    def __str__(self) -> str:
        return f"{self.username} [{self.email}]"


# User tendra un campo dinamico llamado 'order_set' dado que hay una relacion
# entre un order y un user


class Client(models.Model):
    dni = models.CharField(max_length=8)
    first_name = models.CharField(max_length=50, default=None)
    last_name = models.CharField(max_length=50, default=None)
    phone = models.CharField(max_length=50, default=None)
    address = models.CharField(max_length=50, default=None)
    company = models.CharField(max_length=50, default=None)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.dni} {self.company}"


class Sale(models.Model):
    code = models.CharField(max_length=20)
    description = models.TextField(max_length=100, default=None)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField()


class Provider(models.Model):
    first_name = models.CharField(max_length=50, default=None)
    last_name = models.CharField(max_length=50, default=None)
    address = models.CharField(max_length=50, default=None)
    company = models.CharField(max_length=50, default=None)


class Product(models.Model):
    code = models.CharField(max_length=20)
    description = models.TextField(max_length=100, default=None)
    stock = models.IntegerField(default=0)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, default=None)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)


class Order(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=0)
