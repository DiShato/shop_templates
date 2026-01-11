from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Product
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'shop/templates/shop/home.html')

class ProductListView(ListView):
    model = Product
    template_name = 'shop/templates/shop/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/templates/shop/product_detail.html'

    def get(self, request, *args, **kwargs):
        """Функция перехватывает ошибку 404 при переходе неа страницу детализации товара и перенаправляет на страницу списка товаров"""
        try:
            self.object = self.get_object()
        except Http404:
            return redirect('product_list')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    