from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('<str:key_type>', views.get_zodiac_type),
    path('type/<str:zodiac_type>', views.get_zodiac_sign_of_type, name='zodiac_type_name'),
    path('<int:sign_zodiac>', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>', views.get_info_about_zodiac_sign, name='horoscope_name'),
    path('<int:month>/<int:day>', views.get_zodiac_sign_by_date),
]


