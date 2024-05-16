from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product, Contact


class ProductCreateView(CreateView):
    model = Product
    fields = (
        "name", "description", "photo", "category",
        "price", "created_at", "updated_at"
    )
    success_url = reverse_lazy("catalog:page_1")


class Product1ListView(ListView):
    model = Product
    template_name = "catalog/home_1.html"


class Product2ListView(ListView):
    model = Product
    template_name = "catalog/home_2.html"


class ProductDetailListView(DetailView):
    model = Product
    template_name = "catalog/catalog_detail.html"


def home(request):
    context = {
        "title": 'Главная страница'
    }
    return render(request, "catalog/home.html", context)


def contacts(request):
    contact_list = Contact.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        Contact.objects.create(name=name, phone=phone, message=message)

        print(f"\n\nИмя - {name}\n" f"Телефон - {phone}\n" f"Сообщение - {message}\n\n")

    context = {
        'object_list': contact_list,
        "title": 'Контакты'
    }

    return render(request, "catalog/contact.html", context)
