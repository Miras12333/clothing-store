from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Jeans(models.Model):
    name = models.CharField('Title', max_length = 40)
    price = models.FloatField('Price')
    photo = models.ImageField(upload_to='Jeans/', default="a")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Jeans'
        verbose_name_plural = 'Jeans'

class Shirts(models.Model):
    name = models.CharField('Title', max_length = 40)
    price = models.FloatField('Price')
    photo = models.ImageField(upload_to='Shirts/', default="a")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Shirt'
        verbose_name_plural = 'Shirts'

class T_shirts(models.Model):
    name = models.CharField('Title', max_length = 40)
    price = models.FloatField('Price')
    photo = models.ImageField(upload_to='T-shirts', default="a")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'T-shirt'
        verbose_name_plural = 'T-shirts'

class Jackets(models.Model):
    name = models.CharField('Title', max_length = 40)
    price = models.FloatField('Price')
    photo = models.ImageField(upload_to='Jackets/', default="a")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Jacket'
        verbose_name_plural = 'Jackets'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    items = models.TextField()  


    def __str__(self):
        return f"Order {self.pk} by {self.user.username}"
    
class ContactMessage(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email')
    reason = models.CharField('Reason', max_length=100)
    message = models.TextField('Message', max_length=500)

    def __str__(self):
        return self.name