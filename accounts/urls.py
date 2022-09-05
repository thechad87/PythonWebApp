from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('customer/<str:pk>/', views.customer),
    path('products/',views.products),
    path('profile/',views.profile),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('create_order/', views.createOrder, name ="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name ="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name ="delete_order"),


]