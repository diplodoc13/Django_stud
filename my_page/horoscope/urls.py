from django.urls import path, register_converter
from . import views, converters


register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')


urlpatterns = [
    path('', views.index, name='horoscope_index'),
    # path('<str:key_type>', views.get_zodiac_type),
    path('type/<str:zodiac_type>', views.get_zodiac_sign_of_type, name='zodiac_type_name'),
    path('<yyyy:sign_zodiac>', views.get_yyyy_converters),
    path('<int:sign_zodiac>', views.get_info_about_zodiac_sign_by_number),
    path('<my_float:sign_zodiac>', views.get_my_float_converters),
    path('<my_date:sign_zodiac>', views.get_my_date_converters),
    path('<str:sign_zodiac>', views.get_info_about_zodiac_sign, name='horoscope_name'),
    path('<int:month>/<int:day>', views.get_zodiac_sign_by_date),
]


