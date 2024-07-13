from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .models import Customer, Product, Cart, Payment, OrderPlaced, Wishlist
from django.db.models import Count, Q
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.conf import settings
import stripe

# Configure Stripe with the secret API key from settings.
stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    """Render the home page."""
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/home.html', locals())

def about(request):
    """Render the about page."""
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        wishitem = len(Wishlist.objects.filter(user=request.user))
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/about.html', locals())

def contact(request):
    """Render the contact page."""
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        wishitem = len(Wishlist.objects.filter(user=request.user))
        totalitem = len(Cart.objects.filter(user=request.user))    
    return render(request, 'app/contact.html', locals())

class CategoryView(View):
    """View to display products by category."""
    def get(self, request, val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            wishitem = len(Wishlist.objects.filter(user=request.user))
            totalitem = len(Cart.objects.filter(user=request.user))
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())

class CategoryTitle(View):
    """View to display products by title within a category."""
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            wishitem = len(Wishlist.objects.filter(user=request.user))
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, "app/category.html", locals())

class ProductDetail(View):
    """View to display detailed information about a single product."""
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, "app/productdetail.html", locals())

class CustomerRegistrationView(View):
    """View to handle customer registration."""
    def get(self, request):
        form = CustomerRegistrationForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            wishitem = len(Wishlist.objects.filter(user=request.user))
            totalitem = len(Cart.objects.filter(user=request.user))
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
    """View to handle customer profile."""
    def get(self, request):
        form = CustomerProfileForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            wishitem = len(Wishlist.objects.filter(user=request.user))
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/profile.html', {'form': form})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            # Save the customer's profile details.
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
    """View to display the customer's addresses."""
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        wishitem = len(Wishlist.objects.filter(user=request.user))
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/address.html', {'add': add})

class UpdateAddress(View):
    """View to update a customer's address."""
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            wishitem = len(Wishlist.objects.filter(user=request.user))
            totalitem = len(Cart.objects.filter(user=request.user))
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
    """Add a product to the customer's cart."""
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

def show_cart(request):
    """Display the customer's cart."""
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 1000  # Adjust the additional charge as necessary
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/addtocart.html', locals())

class Checkout(View):
    """View to handle the checkout process."""
    def post(self, request):
        user = request.user
        cart_items = Cart.objects.filter(user=user)
        famount = sum(p.quantity * p.product.discounted_price for p in cart_items)
        totalamount = famount + 1000  # Adjust the additional charge as necessary
        stripeamount = int(totalamount * 100)  # Stripe amount in kobo

        try:
            # Create a Stripe checkout session.
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
            # Save the payment details.
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
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))

        context = {
            'add': add,
            'cart_items': cart_items,
            'totalamount': totalamount,
        }
        return render(request, 'app/checkout.html', context)

def payment_done(request):
    """Handle the payment success scenario."""
    session_id = request.GET.get('session_id')
    user = request.user
    
    try:
        # Retrieve the Stripe checkout session.
        checkout_session = stripe.checkout.Session.retrieve(session_id)
        payment_intent = checkout_session['payment_intent']
        payment = Payment.objects.get(stripe_order_id=session_id)
        payment.stripe_payment_id = payment_intent
        payment.paid = True
        payment.save()
        
        # Save the order details.
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
    """Render the payment cancellation page."""
    return render(request, 'app/cancel.html')

def orders(request):
    """Display the customer's orders."""
    order_placed = OrderPlaced.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        wishitem = len(Wishlist.objects.filter(user=request.user))
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/orders.html', locals())

def plus_cart(request):
    """Increase the quantity of a product in the cart."""
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
        totalamount = amount + 1000  # Adjust the additional charge as necessary
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

def minus_cart(request):
    """Decrease the quantity of a product in the cart."""
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
        totalamount = amount + 1000  # Adjust the additional charge as necessary
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

def remove_cart(request):
    """Remove a product from the cart."""
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

def plus_wishlist(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user, product=product).save()
        data = {
            'message': 'Wishlist Added Successfully',
        }
        return JsonResponse(data)
    
def minus_wishlist(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user, product=product).delete()
        data = {
            'message': 'Wishlist remove Successfully',
        }
        return JsonResponse(data)