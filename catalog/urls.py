from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductCreateView, ProductListView, \
    ProductDetailListView, ContactListView, ContactCreateView, HomeTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('1/', ProductListView.as_view(), name='page_1'),
    path('contacts/', ContactListView.as_view(), name='contacts_list'),
    path('support/', ContactCreateView.as_view(), name='support'),
    path('detail/<int:pk>/', ProductDetailListView.as_view(), name='detail_product'),
    path('add_product/', ProductCreateView.as_view(), name='create_product'),
]
