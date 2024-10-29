from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Nombre del producto
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio original
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Precio con descuento
    image_url = models.URLField(max_length=200, null=True, blank=True)  # URL de la imagen del producto

    def __str__(self):
        return self.name  # Representación del objeto como su nombre


class Contact(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del contacto
    email = models.EmailField()  # Email del contacto
    mensaje = models.TextField()  # Mensaje del contacto

    def __str__(self):
        return self.nombre  # Representación del objeto como el nombre


class Carrito(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)  # Relación con el modelo Product
    nombre_producto = models.CharField(max_length=255)  # Nombre del producto en el carrito
    cantidad = models.IntegerField()  # Cantidad del producto en el carrito
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total de la compra para este producto
# Create your models here.
