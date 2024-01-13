from django.contrib import admin
from .models import Cart, CartItem, Jeans, T_shirts, Shirts, Jackets, Order, ContactMessage

admin.site.register(Jeans)
admin.site.register(T_shirts)
admin.site.register(Shirts)
admin.site.register(Jackets)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(ContactMessage)