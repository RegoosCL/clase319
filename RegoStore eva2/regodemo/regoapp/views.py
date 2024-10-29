from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, UserUpdateForm
from .models import Contact, Product, Carrito
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')  # Renderiza la página de inicio

def about(request):
    return render(request, 'about.html')  # Renderiza la página "Acerca de"

@login_required
def modificar_usuario(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)  # Formulario para actualizar datos de usuario
        if form.is_valid():
            form.save()  # Guarda los cambios
            messages.success(request, 'Tu perfil ha sido actualizado con éxito.')
            return redirect('perfil_usuario')  # Redirige al perfil del usuario
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'modificar_usuario.html', {'form': form})

def perfil_usuario(request):
    return render(request, 'perfil_usuario.html')  # Renderiza el perfil del usuario

@login_required
def eliminar_usuario(request):
    user = request.user
    user.delete()  # Elimina el usuario
    messages.success(request, 'Tu perfil ha sido eliminado con éxito.')
    return redirect('home')  # Redirige a la página de inicio

def products(request):
    products = Product.objects.all()  # Obtiene todos los productos
    return render(request, 'products.html', {'products': products})

def contact(request):
    if request.method == 'POST':
        # Procesa el formulario de contacto
        nombre = request.POST.get('name')
        email = request.POST.get('email')
        mensaje = request.POST.get('message')

        Contact.objects.create(nombre=nombre, email=email, mensaje=mensaje)  # Crea un nuevo contacto
        messages.success(request, 'Mensaje enviado con éxito.')
        return redirect('contact')

    return render(request, 'contact.html')  # Renderiza la página de contacto

def carrito(request):
    cart = request.session.get('cart', {})  # Obtiene el carrito de la sesión
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())  # Calcula el precio total
    return render(request, 'carrito.html', {'cart': cart, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Obtiene el producto
    cart = request.session.get('cart', {})  # Obtiene el carrito de la sesión

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1  # Incrementa la cantidad si el producto ya está en el carrito
    else:
        cart[str(product_id)] = {  # Agrega el producto al carrito
            'name': product.name,
            'price': float(product.price),
            'quantity': 1
        }

    request.session['cart'] = cart  # Guarda el carrito en la sesión
    request.session.modified = True  # Marca la sesión como modificada
    return redirect('products')

def eliminar_del_carrito(request, producto_id):
    cart = request.session.get('cart', {})  # Obtiene el carrito
    if str(producto_id) in cart:
        del cart[str(producto_id)]  # Elimina el producto del carrito
        request.session.modified = True  # Marca la sesión como modificada
    return redirect('carrito')  # Redirige al carrito

@login_required
def comprar(request, producto):
    cart = request.session.get('cart', {})  # Obtiene el carrito
    producto_id = str(producto)

    if producto_id in cart:
        producto_obj = get_object_or_404(Product, id=producto)  # Obtiene el producto
        cantidad = cart[producto_id]['quantity']
        precio = cart[producto_id]['price']
        total = cantidad * precio  # Calcula el total de la compra

        # Crea el objeto Carrito en la base de datos
        Carrito.objects.create(
            producto=producto_obj,
            nombre_producto=producto_obj.name,  
            cantidad=cantidad,
            precio=precio,
            total=total
        )

        del cart[producto_id]  # Elimina el producto del carrito
        request.session.modified = True  # Marca la sesión como modificada
        messages.success(request, 'Compra realizada con éxito.')
    else:
        messages.error(request, 'El producto no está en el carrito.')

    return redirect('carrito')  # Redirige al carrito

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # Procesa el formulario de registro
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario
            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario {username} creado con éxito.')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})  # Renderiza la página de registro

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # Autentica al usuario
        if user is not None:
            login(request, user)  # Inicia sesión
            return redirect('home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña no son validos')
    return render(request, 'login.html')  # Renderiza la página de inicio de sesión

@login_required
def user_logout(request):
    logout(request)  # Cierra sesión
    return redirect('home')  # Redirige a la página de inicio

# Create your views here.
