from django.urls import path
from Product.apps import ProductConfig

from Product.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ContactsView

app_name = ProductConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='single_product'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactsView.as_view()),
]
