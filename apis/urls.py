from django.urls import path
from .views import *

urlpatterns = [
    # Dishes
    path('', DishListAPIView.as_view(), name='menu-list'),
    path('menu/create/', DishCreateAPIView.as_view(), name='menu-create'),
    path('menu/<int:pk>/', DishRetrieveUpdateAPIView.as_view(), name='menu-detail'),
    path('menu/<int:pk>/delete/', DishDestroyAPIView.as_view(), name='menu-delete'),
    # Tables
    path('tables/', TableListAPIView.as_view(), name='table-list'),
    path('table/create/', TableCreateAPIView.as_view(), name='table-create'),
    path('table/<int:pk>/', TableRetrieveUpdateAPIView.as_view(), name='table-detail'),
    path('table/<int:pk>/delete/', TableDestroyAPIView.as_view(), name='table-delete'),
    # Bills 
    path('bills/', BillListAPIView.as_view(), name='bill-list'),
    path('bill/create/', BillCreateAPIView.as_view(), name='bill-create'),
    path('bill/<int:pk>/', BillRetrieveUpdateAPIView.as_view(), name='bill-detail'),
    path('bill/<int:pk>/delete/', BillDestroyAPIView.as_view(), name='bill-delete'),
    # Orders
    path('orders/', OrderListAPIView.as_view(), name='order-list'),
    path('order/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('order/<int:pk>/', OrderRetrieveUpdateAPIView.as_view(), name='order-detail'),
    path('order/<int:pk>/delete/', OrderDestroyAPIView.as_view(), name='order-delete'),
]
