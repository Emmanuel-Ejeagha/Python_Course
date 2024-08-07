from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib import auth
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator

# Create your views here.

# username validation
class UsernameValidationView(View):
    def post(self, request):
        data=json.loads(request.body)
        username = data['username']
        
        # checks if the user enters a non alphanumeric character
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        
        # checks if username already exist in the database
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'sorry, username already exists, choose another one'}, status=409)
        return JsonResponse({'username_valid': True})


# Email validation
class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry email already exist, choose another email'})
        return JsonResponse({'email_valid': True})
        
        

# renders the register page
class RegistrationView(View):
    def get(self, request):
        return render(request, "authentication/register.html")
    
    def post(self, request):
       # GET USER DATA
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       context = {
          'fieldValues': request.POST 
       }
       
    #    Validate Username
       if not User.objects.filter(username=username).exists():
           if not User.objects.filter(email=email).exists():
               if len(password) < 6:
                   messages.error(request, 'Password too short')
                   return render(request, "authentication/register.html", context)
               
               user = User.objects.create_user(username=username, email=email)
               user.set_password(password)
               user.set_password = False
               user.save()
               
            #    path_to_view
               # - getting domain we are on
               # - relative url to verification
               # - encode uid
               # - token
               
               uidb64 = force_bytes(urlsafe_base64_encode(user.pk))
               domain = get_current_site(request).domain
               link=reverse('activate', kwargs={'uidb64': uidb64, 'token': token_generator})
               
               activate_url = 'http://'+domain+link
               
               email_body = 'Hi '+user.username+"Please use this link to verify your account\n" + activate_url
               email_subject = 'Activate your account'
               
               email = EmailMessage(
                   email_subject,
                   email_body,
                   'noreply@monywealth.com',
                   [email],
               )
               
               email.send(fail_silently=False)
               messages.success(request, 'Account created successfully')
               return render(request, "authentication/register.html")
       

           
       return render(request, "authentication/register.html")
   
class VerificationView(View):
    def get(self, request, uidb64, token):
        return redirect('login')