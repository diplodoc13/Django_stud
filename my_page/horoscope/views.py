from datetime import date

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from django.urls import reverse

zodiac_dict = {
    'aries':
        {'description': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
         'types': 'fire',
         'day_start': 21,
         'month_start': 3,
         'day_finish': 20,
         'month_finish': 4,
         'si': 'aries'
         },
    'taurus':
        {'description': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
         'types': 'earth',
         'day_start': 21,
         'month_start': 4,
         'day_finish': 21,
         'month_finish': 5,
         'si': 'taurus'
         },
    'gemini':
        {'description': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
         'types': 'air',
         'day_start': 22,
         'month_start': 5,
         'day_finish': 21,
         'month_finish': 6,
         'si': 'gemini'
         },
    'cancer':
        {'description': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
         'types': 'water',
         'day_start': 22,
         'month_start': 6,
         'day_finish': 22,
         'month_finish': 7,
         'si': 'cancer'
         },
    'leo':
        {'description': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
         'types': 'fire',
         'day_start': 23,
         'month_start': 7,
         'day_finish': 21,
         'month_finish': 8,
         'si': 'leo'
         },
    'virgo':
        {'description': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
         'types': 'earth',
         'day_start': 22,
         'month_start': 8,
         'day_finish': 23,
         'month_finish': 9,
         'si': 'virgo'
         },
    'libra':
        {'description': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
         'types': 'air',
         'day_start': 24,
         'month_start': 9,
         'day_finish': 23,
         'month_finish': 10,
         'si': 'libra'
         },
    'scorpio':
        {'description': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
         'types': 'water',
         'day_start': 24,
         'month_start': 10,
         'day_finish': 22,
         'month_finish': 11,
         'si': 'scorpio'
         },
    'sagittarius':
        {'description': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
         'types': 'fire',
         'day_start': 23,
         'month_start': 11,
         'day_finish': 22,
         'month_finish': 12,
         'si': 'sagittarius'
         },
    'capricorn':
        {'description': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
         'types': 'earth',
         'day_start': 23,
         'month_start': 12,
         'day_finish': 20,
         'month_finish': 1,
         'si': 'capricorn'

         },
    'aquarius':
        {'description': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
         'types': 'air',
         'day_start': 21,
         'month_start': 1,
         'day_finish': 19,
         'month_finish': 2,
         'si': 'aquarius'
         },
    'pisces':
        {'description': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
         'types': 'water',
         'day_start': 20,
         'month_start': 2,
         'day_finish': 20,
         'month_finish': 3,
         'si': 'pisces'
         }
}
# zodiac_dict = {
#     'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
#     'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
#     'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
#     'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
#     'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
#     'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
#     'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
#     'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
#     'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22',
#     'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
#     'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
#     'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'
# }

type_zodiac_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'eath': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из 4х цифр - {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число - {sign_zodiac}')


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату - {sign_zodiac}')


def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope_name', args=[sign])
        li_elements += f'<li> <a href="{redirect_path}"> {sign.title()} </a> </li>'
    response = f'''
    <ul>
        {li_elements}
    </ul>
    '''
    return HttpResponse(response)


def get_zodiac_sign_of_type(request, zodiac_type):
    zodiac_sign_of_type = type_zodiac_dict.get(zodiac_type)
    li_elements = ''
    for zodiac in zodiac_sign_of_type:
        redirect_path = reverse('horoscope_name', args=[zodiac])
        li_elements += f'<li> <a href="{redirect_path}"> {zodiac.title()} </a> </li>'
    response = f'''
            <ul>
                {li_elements}
            </ul>
            '''
    return HttpResponse(response)


# def get_info_about_zodiac_sign(request, sign_zodiac: str):
#     if sign_zodiac == "type":
#         types = list(type_zodiac_dict)
#         li_elements = ''
#         for h_type in types:
#             redirect_path = reverse('zodiac_type_name', args=[h_type])
#             li_elements += f'\n<li> <a href="{redirect_path}"> {h_type.title()} </a> </li>'
#         response = f'''
#             <ul>
#                 {li_elements}
#             </ul>
#             '''
#         return HttpResponse(response)
#     description = zodiac_dict.get(sign_zodiac, None).get('description')
#     response1 = render_to_string('horoscope/info_zodiac.html')
#     if description:
#         return HttpResponse(description)
#     else:
#         return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_zodiac}")

def get_info_about_zodiac_sign(request, sign_zodiac: str):
    if sign_zodiac == "type":
        types = list(type_zodiac_dict)
        li_elements = ''
        for h_type in types:
            redirect_path = reverse('zodiac_type_name', args=[h_type])
            li_elements += f'\n<li> <a href="{redirect_path}"> {h_type.title()} </a> </li>'
        response = f'''
            <ul>
                {li_elements}
            </ul>
            '''
        return HttpResponse(response)
    description = zodiac_dict[sign_zodiac]['description']
    sign = zodiac_dict[sign_zodiac]['si'].title()
    data = {
        'sign': sign,
        'dz': description,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_zodiac_sign_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac not in range(1, 13):
        return HttpResponseNotFound(f'Incorrect number of sign zodiac')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope_name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def get_zodiac_sign_by_date(request, month: int, day: int):
    if month > 12 or day > 31:
        return HttpResponseNotFound(f'Incorrect date month {month} day {day}')
    else:
        for i in zodiac_dict:
            if (zodiac_dict[i]['day_start'] <= day and zodiac_dict[i][
                'month_start'] == month) or (
                    zodiac_dict[i]['day_finish'] >= day and zodiac_dict[i]['month_finish'] == month):
                return HttpResponseRedirect(reverse('horoscope_name', args=[zodiac_dict[i]['si']]))
