from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import History
from .serializers import HistorySerializer


class ListHistory(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class DetailHistory(generics.RetrieveAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
