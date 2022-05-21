from django.urls import path

from . import views

urlpatterns = [
    path('square/<int:side>', views.get_square_area, name='square_name'),
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area, name='rectangle_name'),
    path('circle/<int:radius>', views.get_circle_area, name='circle_name'),
    path('get_square_area/<int:side>', views.get_square_by_function),
    path('get_rectangle_area/<int:width>/<int:height>', views.get_rectangle_by_function),
    path('get_circle_area/<int:radius>', views.get_circle_by_function),
]
