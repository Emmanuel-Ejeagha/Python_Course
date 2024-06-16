from django.shortcuts import render
from urllib import request
from django.views import View

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

class CategoryView(View):
    def get(self, request):
        return render(request, "app/category.html")
