from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductCreateView, ProductListView, \
    ProductDetailListView, ContactListView, ContactCreateView, HomeTemplateView, ProductUpdateView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('', ProductListView.as_view(), name='page_1'),
    path('contacts/', ContactListView.as_view(), name='contacts_list'),
    path('support/', ContactCreateView.as_view(), name='support'),
    path('detail/<int:pk>/', cache_page(60)(ProductDetailListView.as_view()), name='detail_product'),
    path('add_product/', ProductCreateView.as_view(), name='create_product'),
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('category', CategoryListView.as_view(), name='category_list'),
]
