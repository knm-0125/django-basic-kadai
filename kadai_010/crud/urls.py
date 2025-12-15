from django.urls import path
from .views import TopView, ProductDetailView

urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('list/' ProductListView.as_view(), name='product_list')
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]