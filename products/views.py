from django.shortcuts import render
from .models import Product

def product_list(request):
    category = request.GET.get('category', '')
    q = request.GET.get('q', '')
    products = Product.objects.all()
    if category:
        products = products.filter(category=category)
    if q:
        products = products.filter(name__icontains=q)

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': Product.CATEGORY_CHOICES,
        'active_category': category,
        'query': q,
        'meta_title': 'Products — Tiles, Granite & Sanitaryware | Srinivasa Tiles',
        'meta_description': 'Browse vitrified tiles, bathroom tiles, granite, and sanitaryware. Enquire on WhatsApp.',
    })
