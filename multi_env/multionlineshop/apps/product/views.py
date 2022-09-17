import random

from django.shortcuts import render, get_object_or_404


from .models import Category, Product

def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category_slug=category_slug, slug=product_slug)

    similar_products = list(product.category.products.excludes(id=product.id))

    if len(similar_products) >=4 :
        similar_products = random.sample(similar_products, 4)
    
    return render(request,'product/product.html', {'product':product, 'similar_products': similar_products})
    