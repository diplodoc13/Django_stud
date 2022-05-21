from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def get_square_area(request, side: int):
    result = side**2
    return HttpResponse(f'Площадь квадрата размером {side}x{side} равна {result}')

def get_rectangle_area(request, width: int, height: int):
    result = width * height
    return HttpResponse(f'Площадь прфмоугльника размером {width}x{height} равна {result}')

def get_circle_area(request, radius: int):
    result = 3.14 * radius
    return HttpResponse(f'Площадь круга с радиусом {radius} равна {result}')

def get_square_by_function(request, side: int):
    redirect_url_square = reverse("square_name", args=[side])
    return HttpResponseRedirect(redirect_url_square)
def get_rectangle_by_function(request, width: int, height: int):
    redirect_url_rectangle = reverse("rectangle_name", args=[width, height])
    return HttpResponseRedirect(redirect_url_rectangle)
def get_circle_by_function(request, radius: int):
    redirect_url_circle = reverse("circle_name", args=[radius])
    return HttpResponseRedirect(redirect_url_circle)
