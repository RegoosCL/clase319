"""
URL configuration for regodemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from regoapp import views


urlpatterns = [
    path('admin/', admin.site.urls),  # URL para acceder al panel de administración
    path('', views.home, name='home'),  # Página de inicio
    path('about/', views.about, name='about'),  # Página "Quiénes Somos"
    path('products/', views.products, name='products'),  # Página de productos
    path('contact/', views.contact, name='contact'),  # Página de contacto
    path('login/', views.user_login, name='login'),  # Página de inicio de sesión
    path('logout/', views.user_logout, name='user_logout'),  # URL para cerrar sesión
    path('register/', views.register, name='register'),  # Página de registro
    path('carrito/', views.carrito, name='carrito'),  # Página del carrito de compras
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Añadir producto al carrito
    path('eliminar_del_carrito/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),  # Eliminar producto del carrito
    path('comprar/<int:producto>/', views.comprar, name='comprar'),  # Comprar producto
    path('modificar_usuario/', views.modificar_usuario, name='modificar_usuario'),  # Modificar perfil de usuario
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),  # Ver perfil de usuario
    path('eliminar_usuario/', views.eliminar_usuario, name='eliminar_usuario'),  # Eliminar perfil de usuario
]