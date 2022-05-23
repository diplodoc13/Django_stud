from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

week_days_dict = {
    "monday": "Список дел на Понедельник:",
    "tuesday": "Список дел на Вторник:",
    "wednesday": "Список дел на Среду:",
    "thursday": "Список дел на Четверг:",
    "friday": "Список дел на Пятницу:",
    "saturday": "Список дел на Субботу:",
    "sunday": "Список дел на Воскресенье:",
}


def get_info_about_week_day(request, day_of_the_week: str):
    description = week_days_dict.get(day_of_the_week, None)
    if description:
        return render(request, 'week_days/greeting.html',)
    else:
        return HttpResponseNotFound(f"Неизвестный день недели - {day_of_the_week}")


def get_info_about_week_day_by_number(request, day_of_the_week: int):
    list_of_week_days = list(week_days_dict)
    if day_of_the_week not in range(1, 8):
        return HttpResponse(f"Unknoun day of the week: {day_of_the_week}")
    number_of_day = list_of_week_days[day_of_the_week - 1]
    redirect_url = reverse('name_day_of_the_week', args=[number_of_day])
    return HttpResponseRedirect(redirect_url)
