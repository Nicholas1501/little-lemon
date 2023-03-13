from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking
from .models import Menu
from rest_framework import generics
from .serializers import MenuSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def home(request):
    return

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer