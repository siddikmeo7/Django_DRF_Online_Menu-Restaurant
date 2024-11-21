from django.urls import path
from .views import *

urlpatterns = [
    # Dishes
    path('', DishListAPIView.as_view(), name='dish-list'),
    path('dishes/create/', DishCreateAPIView.as_view(), name='dish-create'),
    path('dishes/<int:pk>/', DishRetrieveUpdateAPIView.as_view(), name='dish-detail'),
    path('dishes/<int:pk>/delete/', DishDestroyAPIView.as_view(), name='dish-delete'),
    # Tables
    path('tables/', TableListAPIView.as_view(), name='table-list'),
    path('tables/create/', TableCreateAPIView.as_view(), name='table-create'),
    path('tables/<int:pk>/', TableRetrieveUpdateAPIView.as_view(), name='table-detail'),
    path('tables/<int:pk>/delete/', TableDestroyAPIView.as_view(), name='table-delete'),
    # Bills 
    path('bills/', BillListAPIView.as_view(), name='bill-list'),
    path('bills/create/', BillCreateAPIView.as_view(), name='bill-create'),
    path('bills/<int:pk>/', BillRetrieveUpdateAPIView.as_view(), name='bill-detail'),
    path('bills/<int:pk>/delete/', BillDestroyAPIView.as_view(), name='bill-delete'),
    # Orders
    path('orders/', OrderListAPIView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateAPIView.as_view(), name='order-detail'),
    path('orders/<int:pk>/delete/', OrderDestroyAPIView.as_view(), name='order-delete'),
]
