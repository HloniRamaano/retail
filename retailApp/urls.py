from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),

    #Product API's
    path('product-list/', views.productList, name="product-list"),
    path('product-detail/<str:pk>/', views.productDetail, name="product-detail"),
    path('product-create/', views.productCreate, name="product-create"),
    path('product-update/<str:pk>/', views.productUpdate, name="product-update"),
    path('product-delete/<str:pk>/', views.productDelete, name="product-delete"),

    #Shopping Cart API's
    path('shopping-cart-list/', views.shoppingCartList, name="shopping-cart-list"),
    path('shopping-cart-add/', views.shoppingCartCreate, name="shopping-cart-add"),

    #Payment API's
    path('payment-list/', views.paymentList, name="payment-list"),
    path('payment-create/', views.paymentCreate, name="payment-create"),
    
    
    #Account Api's
    path('account-create/',views.accountCreate, name="account-create"),
    path('account-list/', views.accountList, name="account-list"),
    path('account-update/<str:pk>/', views.accountUpdate, name="account-update"),
    
        
    #Front end urls
    path('home/',views.home_view, name='home'),
    path('register/',views.registration_view, name='register'),
]