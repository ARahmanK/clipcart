from math import ceil

from django.shortcuts import render

from .models import Product,Contact


def shop(requests):
    products_sub_cats = Product.objects.values('category')
    prods = []
    cats = {item['category'] for item in products_sub_cats}
    for cat in cats:
        cat_product = Product.objects.filter(category=cat)
        n = len(cat_product)
        slides = n // 4 + ceil((n / 4) - (n // 4))
        prods.append([cat_product, slides, range(slides)])

    # params = {'products': products, 'slides': slides, 'range': range(slides)}
    params = {'prods': prods}
    return render(requests, 'shop/index.html', params)

def product_view(requests,myid):
    product = Product.objects.filter(id=myid)
    params = {'product':product[0]}
    return render(requests, 'shop/product.html',params)

def about(requests):
    return render(requests, 'shop/about.html')

def contact(requests):
    if requests.method=='POST':
        name = requests.POST.get('name','')
        email = requests.POST.get('email','')
        phone = requests.POST.get('phone','')
        message = requests.POST.get('msg','')
        contact = Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
    return render(requests, 'shop/contact.html')
