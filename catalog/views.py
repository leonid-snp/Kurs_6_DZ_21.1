from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from catalog.form import ProductForm
from catalog.models import Product, Contact
from version.models import Version


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:page_1")


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        list_product = Product.objects.all()

        for product in list_product:
            version = Version.objects.filter(product=product)
            activ_version = version.filter(is_activ=True)
            if activ_version:
                product.active_version = activ_version.last().name
                product.number_version = activ_version.last().number
            else:
                product.active_version = 'Нет активной версии'

        context_data['object_list'] = list_product
        return context_data


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
