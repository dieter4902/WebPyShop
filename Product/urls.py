from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.product_list, name='all-products'),
    path('show/<int:pk>/', views.product_detail, name='product-detail'),
    path('show/<int:pk>/vote/<str:up_or_down>/', views.vote, name='product-vote'),
    path('add/', views.product_create, name='product-create'),
    path('delete/<int:pk>/', views.product_delete, name='product-delete'),
]