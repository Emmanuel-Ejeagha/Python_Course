from django.contrib import admin
from . models import Product, Customer, Cart, Payment, OrderPlaced, Wishlist
from django.utils.html import format_html
from django.contrib.auth.models import Group
from django.urls import reverse
# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'product_image']
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode'] 
    
    
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']
    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html(',a href="{}">{}</a>', link, obj.product.title)
    
@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'stripe_order_id', 'stripe_payment_status', 'stripe_payment_id', 'paid']
    
    
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customers', 'products', 'quantity', 'ordered_date', 'status', 'payments']
    def customers(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html(',a href="{}">{}</a>', link, obj.customer.name)

    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html(',a href="{}">{}</a>', link, obj.product.title)
    
    def payments(self, obj):
        link = reverse("admin:app_payment_change", args=[obj.payment.pk])
        return format_html(',a href="{}">{}</a>', link, obj.payment.stripe_payment_id)

    
    
@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products']
    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html(',a href="{}">{}</a>', link, obj.product.title)


admin.site.unregister(Group)