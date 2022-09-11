from math import ceil

from django.shortcuts import render

from .models import Product


def shop(requests):
    products = Product.objects.all()
    n = len(products)
    slides = n // 3 + ceil((n / 3) - (n // 3))
    params = {'products': products, 'slides': slides, 'range': range(slides)}
    return render(requests, 'shop/index.html', params)


def about(requests):
    return render(requests, 'shop/about.html')
