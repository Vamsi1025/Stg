from django.shortcuts import render
from django.contrib import messages
from products.models import Product
from .forms import ContactForm

def home(request):
    featured = Product.objects.all()[:6]
    categories = [
        {'key': 'vitrified', 'label': 'Vitrified Tiles', 'desc': 'Premium polished finish for elegant interiors.'},
        {'key': 'bathroom', 'label': 'Bathroom Tiles', 'desc': 'Anti-skid, water-resistant designs.'},
        {'key': 'sanitaryware', 'label': 'Sanitaryware', 'desc': 'Modern fittings from top brands.'},
        {'key': 'granite', 'label': 'Granite', 'desc': 'Durable natural stone for every space.'},
    ]
    return render(request, 'core/home.html', {
        'featured': featured,
        'categories': categories,
        'meta_title': 'Srinivasa Tiles & Sanitary — Tiles, Granite & Sanitaryware in Gajuwaka, Vizag',
        'meta_description': 'Premium tiles, granite, and sanitaryware showroom in Gajuwaka, Visakhapatnam. The Next Stage of Luxury. Enquire on WhatsApp.',
    })

def about(request):
    return render(request, 'core/about.html', {
        'meta_title': 'About Us — Srinivasa Tiles & Sanitary',
        'meta_description': 'Trusted tiles and sanitaryware showroom serving Visakhapatnam for years. Quality products, fair prices, expert guidance.',
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Thanks! We'll get back to you shortly.")
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {
        'form': form,
        'meta_title': 'Contact — Srinivasa Tiles & Sanitary, Gajuwaka',
        'meta_description': 'Visit our showroom in Gajuwaka, Visakhapatnam or message us on WhatsApp.',
    })
