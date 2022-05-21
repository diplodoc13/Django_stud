from django.urls import path
from . import views

urlpatterns = [
    path('<int:day_of_the_week>', views.get_info_about_week_day_by_number),
    path('<str:day_of_the_week>', views.get_info_about_week_day, name='name_day_of_the_week'),
]