from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from catalog.form import ProductForm, VersionForm, VersionFormSet, ProductModeratorForm
from catalog.models import Product, Contact
from version.models import Version


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:page_1")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(
            Product, Version, form=VersionForm,
            formset=VersionFormSet, extra=1
        )
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        dog = form.save()
        user = self.request.user
        dog.owner = user
        dog.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:page_1")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(
            Product, Version, form=VersionForm, formset=VersionFormSet, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
            self.success_url = reverse_lazy('catalog:edit_product')

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        return self.render_to_response(
            self.get_context_data(
                form=form,
                formset=formset
            ))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif user.has_perm('catalog.unpublish_a_product') or user.has_perm(
                'catalog.change_description') or user.has_perm('catalog.change_category'):
            return ProductModeratorForm
        else:
            raise PermissionDenied


class ProductListView(ListView):
    paginate_by = 3
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


class ProductDetailListView(LoginRequiredMixin, DetailView):
    model = Product


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ("name", "phone", "message")
    success_url = reverse_lazy("catalog:contacts_list")


class HomeTemplateView(TemplateView):
    template_name = "catalog/home.html"
