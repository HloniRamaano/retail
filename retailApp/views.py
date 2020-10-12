from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from . models import Product, ShoppingCart, Payment,Account
from . serializers import ProductSerializer, ShoppingCartSerializer, PaymentSerializer,AccountSerializer,accountsSerializer

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'Product List': '/product-list/',
        'Detail View': '/product-detail/<str:pk>/',
        'Create Product': '/product-create/',
        'Update Product': '/product-update/<str:pk>/',
        'Delete Product': '/product-delete/<str:pk>/',
        'Shopping Cart List': '/shopping-cart-list/',
        'Shopping Cart Add': 'shopping-cart-add/',
        'Payment List': 'shopping-cart-add/',
        'Payment Create': 'payment-create/',
        'Account Create':'account-create/',
        'Account List' :'account-list/',
        'Account Update' :'/account-update/<str:pk>/',
    }
    
    return Response(api_urls)

#Product API's

@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetail(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def productUpdate(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def productDelete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response("Item Successfully Deleted!!!")

#Shopping Cart API's

@api_view(['GET'])
def shoppingCartList(request):
    shoppingCart = ShoppingCart.objects.all()
    serializer = ShoppingCartSerializer(shoppingCart, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def shoppingCartCreate(request):
    serializer = ShoppingCartSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#Payment API's

@api_view(['GET'])
def paymentList(request):
    payment = Payment.objects.all()
    serializer = PaymentSerializer(payment, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def paymentCreate(request):
    serializer = PaymentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#Account
@api_view(['POST'])
def accountCreate(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successful Registered a new user"
            data['firstname'] = account.firstname
            data['lastname'] = account.lastname
            data['username'] = account.username
            data['email'] = account.email
        else:
            data = serializer.errors
        return Response(data)
    
@api_view(['GET'])
def accountList(request):
    context ="Registered Users!"
    accountlist = Account.objects.values_list('id','firstname', 'lastname','email', 'username', 'date_joined','last_login', 'is_admin', 'is_staff', named=True)
    serializer = accountsSerializer(accountlist, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def accountUpdate(request, pk):
    accountupdate = Account.objects.get(id=pk)
    serializer = accountsSerializer(instance=accountupdate, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    