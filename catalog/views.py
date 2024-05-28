from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from catalog.form import ProductForm
from catalog.models import Product, Contact


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:page_1")


class ProductListView(ListView):
    model = Product


class ProductDetailListView(DetailView):
    model = Product


class ContactListView(ListView):
    model = Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = ("name", "phone", "message")
    success_url = reverse_lazy("catalog:contacts_list")


class HomeTemplateView(TemplateView):
    template_name = "catalog/home.html"
