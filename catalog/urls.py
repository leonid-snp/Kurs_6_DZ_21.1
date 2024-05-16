from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, add_product, \
    Product1ListView, Product2ListView, ProductDetailListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('1/', Product1ListView.as_view(), name='home_1'),
    path('2/', Product2ListView.as_view(), name='home_2'),
    path('contacts/', contacts, name='contacts'),
    path('detail/<int:pk>/', ProductDetailListView.as_view(), name='detail_product'),
    path('add_product/', add_product, name='add_product'),
]
