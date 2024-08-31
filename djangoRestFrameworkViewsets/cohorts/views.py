from django.shortcuts import render
from .models import Cohort
from rest_framework import viewsets
from .serializers import CohortSerializer
from rest_framework.response import Response

class CohortViewSet(viewsets.ViewSet):
    """
    Viewset -> a class based view which doesnot provide any method handlers for your requests
    View -> is either a python function or python class that accepts an HTTP request and returns an HTTP response
    """
    
def list(self, request):
    queryset = Cohort.objects.all()
    serializer = CohortSerializer(queryset, many=True)
    return Response(serializer.data)

def retrieve(self, request, pk=None):
    queryset = Cohort.objects.filter(pk=pk)
    serializer = CohortSerializer(queryset)
    return Response(serializer.data)

def create(self, request):
    queryset = Cohort.objects.create(**request.data)
    serializer = CohortSerializer(queryset)
    return Response(serializer.data)

def update(self, request, pk=None):
    pass

def partial_update(self, request, pk):
    pass
def destroy(self, request, pk):
    pass