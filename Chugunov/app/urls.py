from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='home', kwargs = {'fio': 'Чугунов Дмитрий Александвроич', 'age': '15', 'interes': 'Python'}),
    path('about', views.about, name='about', kwargs = {'city': 'Брянск', 'performance': '4-5', 'like': 'Люблю учить питон'}),
    path('contacts', views.contacts, name='contacts', kwargs = {'Telegram': '@JluTui', 'number': '+79803328307', 'passport': '15 21 573176'}),
]
