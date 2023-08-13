from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer


def index(request):
    return render(request, 'restaurant/index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    search_fields = ['category__title']
    ordering_fields = ['price', 'inventory']

class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    
"""
class bookingview(APIView):
    
    def get(self,request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many = True)
        return Response(serializer.data) # return Json
    
    def post(self,request):
        serializer = bookingSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data})
        


class menuview(APIView):
    
    def get(self,request):
        items = Menu.objects.all()
        serializer = menuSerializer(items, many = True)
        return Response(serializer.data) # return Json
    
    def post(self,request):
        serializer = menuSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data})
"""

