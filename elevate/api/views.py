from django.shortcuts import render
from . models import Product
from . serializers import ProductSerializer, RegistrationSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import status


# from django.http import JsonResponse

@api_view(['GET', 'POST'])
def product_list(request, format=None): # format=None is for creating json-file in browser
    """
    Verarbeitet GET- und POST-Anfragen für alle Produkt.

    Args:
        request (HttpRequest): Die eingehende HTTP-Anfrage.

    Returns:
        Response: JSON-Antwort mit Produktdaten.
    """
    # pass # this catches errors
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

        # return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET', 'PUT', 'DELETE'])
def product(request, pk, format=None):
    """
    Verarbeitet GET-, PUT- und DELETE-Anfragen für ein einzelnes Produkt.

    Args:
        request (HttpRequest): Die eingehende HTTP-Anfrage.
        pk (int): Primärschlüssel des Produkts.

    Returns:
        Response: JSON-Antwort mit Produktdaten.
    """
    try: 
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Seccessfully registered a new user!'
        else:
            data = serializer.errors
        return Response(data)