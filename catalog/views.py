from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from catalog.models import Product, Contact, Category


class Product1ListView(ListView):
    model = Product
    template_name = "catalog/home_1.html"


class Product2ListView(ListView):
    model = Product
    template_name = "catalog/home_2.html"


class ProductDetailListView(DetailView):
    model = Product
    template_name = "catalog/detail_product.html"


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


def add_product(request):
    category_list = Category.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        photo = request.FILES.get("photo")
        category_id = request.POST.get("category")
        category = Category.objects.get(id=category_id)
        price = request.POST.get("price")
        created_at = request.POST.get("created_at")
        updated_at = request.POST.get("updated_at")

        Product.objects.create(
            name=name,
            description=description,
            photo=photo,
            category=category,
            price=price,
            created_at=created_at,
            updated_at=updated_at
        )

    context = {
        'object_list': category_list,
        'title': 'Добавить продукт'
    }
    return render(request, 'catalog/product_form.html', context)
