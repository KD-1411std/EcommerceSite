from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil
# Create your views here.


def index(request):
    #products = Product.objects.all()
    #print(products)
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    #params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    return render(request, 'shop/index.html', params)


def about(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    return render(request, 'shop/about.html', params)


def contact(request):
    if request.method=="POST":
        print(request)
        name= request.POST.get("name", "")
        email= request.POST.get("email", "")
        phone= request.POST.get("phone", "")
        desc= request.POST.get("desc", "")
        #print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone,desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def productView(request):

    return HttpResponse(" we are at productView")

def aboutUs(request):
    return render(request, 'shop/aboutUs.html')