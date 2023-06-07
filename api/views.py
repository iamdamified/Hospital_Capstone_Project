from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Patient

# Create your views here.


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def HomePageApi(request):
    return Response("This is the home page")



