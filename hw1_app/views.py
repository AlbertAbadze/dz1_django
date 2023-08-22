from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)

def text(title, text):
    return f'<h1>Мой сайт на Django</h1>' \
           f'<h2>{title}</h2>' \
           f'<p>{text}</p>'

def general(request):
    title = 'Главная страница'
    body_text = 'Современные технологии достигли такого уровня, что существующая теория обеспечивает широкому кругу (специалистов) участие в формировании своевременного выполнения сверхзадачи. Как уже неоднократно упомянуто, сторонники тоталитаризма в науке ассоциативно распределены по отраслям. Задача организации, в особенности же экономическая повестка сегодняшнего дня создаёт необходимость включения в производственный план целого ряда внеочередных мероприятий с учётом комплекса соответствующих условий активизации.'
    logger.info(f'Page "general" is open')
    return HttpResponse(text(title, body_text))

def about(request):
    title = 'О себе'
    body_text = 'Меня зовут Абадзе Альберт Муратович, я студет унивеситета Geekbrains<br>' \
                'Группа - Программист разработчик языка Python'
    logger.info(f'Page "about" is open')
    return HttpResponse(text(title, body_text))
