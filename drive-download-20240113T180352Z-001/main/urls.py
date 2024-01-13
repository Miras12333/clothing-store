from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.home, name="home"),
    path('cart', views.check_cart, name='check_cart'),
    path('contact', views.contact, name="contact"),
    path('shop1', views.shop1, name="shop1"),
    path('shop2', views.shop2, name="shop2"),
    path('Delivery', views.Delivery, name="Delivery"),
    path('privat', views.privat, name="privat"),
    path('shop3', views.shop3, name="shop3"),
    path('shop4', views.shop4, name="shop4"),
    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name='main/login.html'), name="login"),
    path('logout', LogoutView.as_view(template_name='main/logout.html'), name="logout"),
    path('cart', views.cart, name='my_cart'),
    path('add/<str:item_type>/<int:item_id>/', views.add, name="add"),
    path('checkout', views.checkout, name='checkout'),
    path('contact_form', views.contact_form, name='contact_form')
]
