from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth import login
from .models import Jackets, Jeans, Shirts, T_shirts, Cart, CartItem, Order, ContactMessage
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings

def check_cart(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    return render(request, 'main/cart.html', {'cart_items': cart_items})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:home')
    form = NewUserForm()
    context = {'form':form}
    return render(request, 'main/register.html', context)

def home(request):
    return render(request, 'main/index.html')

def cart(request):
    
    cart_items = CartItem.objects.filter(cart__user=request.user)

    
    total = sum(item.item.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return render(request, 'main/cart.html', context)

def contact(request):
    return render(request, 'main/contact.html')

def shop1(request):
    jackets = Jackets.objects.all()
    return render(request, 'main/clothing.html', {'jackets': jackets})

def shop2(request):
    jeans = Jeans.objects.all()
    return render(request, 'main/shop.html', {'jeans': jeans})


def Delivery(request):
    return render(request, 'main/Delivery.html')

def privat(request):
    return render(request, 'main/privat.html')

def shop3(request):
    t_shirts = T_shirts.objects.all()
    return render(request, 'main/shop3.html', {'t_shirts': t_shirts})

def shop4(request):
    shirts = Shirts.objects.all()
    return render(request, 'main/shop4.html', {'shirts': shirts})

@login_required
def add(request, item_type, item_id):
    
    models_map = {
        'jeans': Jeans,
        'shirts': Shirts,
        't_shirts': T_shirts,
        'jackets': Jackets,
    }

    Model = models_map.get(item_type.lower())
    item = get_object_or_404(Model, pk=item_id)

    cart, created = Cart.objects.get_or_create(user=request.user)
    content_type = ContentType.objects.get_for_model(Model)

    cart_item, cart_item_created = CartItem.objects.get_or_create(
        cart=cart,
        content_type=content_type,
        object_id=item.id,
        defaults={'item': item}
    )

    if not cart_item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('main:my_cart')

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    order = Order.objects.create(user=request.user)
    order_id = order.id  
    
    cart_items = CartItem.objects.filter(cart__user=request.user)

    items_info = []
    total_price = 0

    for cart_item in cart_items:
        item_price = cart_item.item.price
        total_item_price = item_price * cart_item.quantity
        total_price += total_item_price

        item_info = f"{cart_item.item.name} - Цена: {item_price}, Количество: {cart_item.quantity}"
        items_info.append(item_info)

    order.total_price = total_price
    order.items = "\n".join(items_info)  
    order.save()

    cart_items.delete()


    order2 = Order.objects.get(id=order_id)
    price = order2.total_price

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(price * 100),  
                        'product_data': {
                            'name': 'Order',
                            
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://localhost:8000/',
            cancel_url='http://localhost:8000/',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        reason = request.POST.get('reason')
        message = request.POST.get('message')
        
        # Сохраняем данные в базе данных
        ContactMessage.objects.create(
            name=name,
            email=email,
            reason=reason,
            message=message
        )

