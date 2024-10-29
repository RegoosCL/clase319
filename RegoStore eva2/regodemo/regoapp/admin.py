from django.contrib import admin
from regoapp.models import Contact, Product, Carrito

admin.site.register(Product)  # Registro del modelo Product en el panel de administración

admin.site.register(Contact)  # Registro del modelo Contact en el panel de administración

admin.site.register(Carrito)  # Registro del modelo Carrito en el panel de administración

# Register your models here.
