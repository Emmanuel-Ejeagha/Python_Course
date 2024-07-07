from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .models import Customer, Product, Cart, Payment
from django.db.models import Count, Q
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.conf import settings
import stripe

# This is your test secret API key.
stripe.api_key = 'sk_test_51PY72gRpD6bGdybGQPBcOLgrKYKXyr46eHE4ljOBgWw4UO3Atf6R5n0scs9qXyS4Pa3HUXgcaUs4HXjylmqI0oHy00ygM1FDxK'


def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())

class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html", locals())

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html", locals())

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/signup.html', {'form': form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return redirect('login')
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/signup.html', {'form': form})

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            reg = Customer(user=user, name=name, locality=locality, mobile=mobile, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile Saved Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/profile.html', {'form': form})

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add': add})

class UpdateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'app/updateAddress.html', {'form': form})
    
    def post(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(request.POST, instance=add)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect('address')


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 1000
    return render(request, 'app/addtocart.html', locals())

class Checkout(View):
    def get(self, request):
        user = request.user
        add = Customer.objects.filter(user=user)
        # cart_items = Cart.objects.filter(user=user)
        # famount = 0
        # for p in cart_items:
        #     value = p.quantity * p.product.discounted_price
        #     famount = famount + value
        # totalamount = famount + 1000  # Adjust the additional charge as necessary
        # stripeamount = int(totalamount * 100)  # Stripe amount in kobo

        # try:
        #     checkout_session = stripe.checkout.Session.create(
        #         payment_method_types=['card'],
        #         line_items=[
        #             {
        #                 'price_data': {
        #                     'currency': 'ngn',
        #                     'product_data': {
        #                         'name': 'Total Purchase',
        #                     },
        #                     'unit_amount': stripeamount,
        #                 },
        #                 'quantity': 1,
        #             },
        #         ],
        #         mode='payment',
        #         success_url='http://localhost:8000/success/',
        #         cancel_url='http://localhost:8000/cancel/',
        #     )
        #     order_id = checkout_session['id']
        #     order_status = checkout_session['status']
        #     if order_status == 'created':
        #         payment = Payment(
        #             user=user,
        #             amount=totalamount,
        #             stripe_order_id=order_id,
        #             stripe_payment_status = order_status
        #         )
        #         payment.save()
        #     return redirect(checkout_session.url, code=303)
        # except Exception as e:
        #     return JsonResponse({'error': str(e)}, status=400)

        return render(request, 'app/checkout.html', locals())
    
def success(request):
    return render(request, 'app/success.html')

def cancel(request):
    return render(request, 'app/cancel.html')


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        totalamount = amount + 1000
        # print(prod_id)
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        totalamount = amount + 1000
        # print(prod_id)
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        if not prod_id:
            return JsonResponse({'error': 'No product id provided'}, status=400)
        
        carts = Cart.objects.filter(Q(product=prod_id) & Q(user=request.user))
        
        if not carts.exists():
            return JsonResponse({'error': 'Cart item not found'}, status=404)
        
        carts.delete()
        
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity
            amount += value
        totalamount = amount + 40
        data = {
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
