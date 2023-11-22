from django.http import HttpResponse
from django.shortcuts import render


def index(request, fio, age, interes):
    return HttpResponse(f'ФИО:{fio}<br>Возраст:{age}<br>Интересы:{interes}<br>')


def about(request,city, performance, like):
    return HttpResponse(f'Город:{city}<br> Успеваемость в школе:{performance}<br> Любит или не любит учиться:{like}<br>')


def contacts(request, Telegram, number, passport):
    return HttpResponse(f'Телеграмм:{Telegram}<br>Номер телефона:{number}<br>Паспорт:{passport}<br>')
