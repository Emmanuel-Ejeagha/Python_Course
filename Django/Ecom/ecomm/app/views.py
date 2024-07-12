from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .models import Customer, Product, Cart, Payment, OrderPlaced
from django.db.models import Count, Q
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.conf import settings
import stripe

# This is your test secret API key.
# stripe.api_key = 'sk_test_51PY72gRpD6bGdybGQPBcOLgrKYKXyr46eHE4ljOBgWw4UO3Atf6R5n0scs9qXyS4Pa3HUXgcaUs4HXjylmqI0oHy00ygM1FDxK'
stripe.api_key = settings.STRIPE_SECRET_KEY

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
    def post(self, request):
        user = request.user
        cart_items = Cart.objects.filter(user=user)
        famount = sum(p.quantity * p.product.discounted_price for p in cart_items)
        totalamount = famount + 1000  # Adjust the additional charge as necessary
        stripeamount = int(totalamount * 100)  # Stripe amount in kobo

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'ngn',
                        'product_data': {
                            'name': 'Total Purchase',
                        },
                        'unit_amount': stripeamount,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://localhost:8000/success/?session_id={CHECKOUT_SESSION_ID}',
                cancel_url='http://localhost:8000/cancel/',
            )
            payment = Payment(
                user=user,
                amount=totalamount,
                stripe_order_id=checkout_session['id'],
                stripe_payment_status=checkout_session['status']
            )
            payment.save()
            return JsonResponse({'id': checkout_session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def get(self, request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = sum(p.quantity * p.product.discounted_price for p in cart_items)
        totalamount = famount + 1000  # Adjust the additional charge as necessary

        context = {
            'add': add,
            'cart_items': cart_items,
            'totalamount': totalamount,
        }
        return render(request, 'app/checkout.html', context)
    
def payment_done(request):
    session_id = request.GET.get('session_id')
    user = request.user
    
    try:
        checkout_session = stripe.checkout.Session.retrieve(session_id)
        payment_intent = checkout_session['payment_intent']
        payment = Payment.objects.get(stripe_order_id=session_id)
        payment.stripe_payment_id = payment_intent
        payment.paid = True
        payment.save()
        
        # To save order details
        cart_items = Cart.objects.filter(user=user)
        for item in cart_items:
            OrderPlaced(
                user=user,
                customer=payment.user.customer,
                product=item.product,
                quantity=item.quantity,
                payment=payment
            ).save()
            item.delete()
            
        return render(request, 'app/orders.html', {'payment': payment})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def cancel(request):
    return render(request, 'app/cancel.html')

def orders(request):
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', locals())


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
