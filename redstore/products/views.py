from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def base(request):
    return render(request,'base.html')
def list_products(request):
    
    return render(request,'products.html')
def detail_products(request):
    return render(request,'product_details.html')