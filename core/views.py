from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def perfect_paws_home(request):
    return HttpResponse("Perfect Paws is alive!")

