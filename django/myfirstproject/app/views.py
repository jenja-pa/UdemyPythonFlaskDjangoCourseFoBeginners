from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def my_index(request):
    return HttpResponse('Hello world')

def my_about(request):
    return HttpResponse('About Response')

def add(request, a, b):
    return HttpResponse(f'{a} + {b} = {a + b}')

def intro(request, name, age):
    return JsonResponse({'name': name, 'age': age})
