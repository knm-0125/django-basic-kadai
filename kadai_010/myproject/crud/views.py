from django.views.generic import ListView, DetailView
from .models import Product

class TopView(ListView):
    model = Product
    template_name = "top.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    