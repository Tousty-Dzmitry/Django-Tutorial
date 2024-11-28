from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#
# def index(request):
#     return HttpResponse("Hello world")

# использование класса HttpResponse

from django.http import HttpResponse, HttpResponsePermanentRedirect

from django.shortcuts import render

from django.template.response import TemplateResponse

from datetime import datetime

# пример отправки простого текста
# def index(request):
#     return HttpResponse("Главная")
#
#
# def about(request):
#     return HttpResponse("О сайте")
#
#
# def contact(request):
#     return HttpResponse("Контакты")



def index (request):
    host = request.META["HTTP_HOST"]  # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"]  # получаем данные бразера
    path = request.path  # получаем запрошенный путь

    return HttpResponse(f"""
            <p>Host: {host}</p>
            <p>Path: {path}</p>
            <p>User-agent: {user_agent}</p>
        """)


# def about(request):
#     return HttpResponse("<h2>О сайте</h2>")

# c кодом html
# def contact(request):
#     return HttpResponse("<h2>Контакты</h2>")

# если используется kwargs
# def about(request, name, age):
#     return HttpResponse(f"""
#             <h2>О пользователе</h2>
#             <p>Имя: {name}</p>
#             <p>Возраст: {age}</p>
#     """)

# Определение параметров через функцию path
def user(request, name):
    return HttpResponse(f"<h2>Имя: {name}</h2>")
# переадресация
def details(request):
    return HttpResponsePermanentRedirect("/index")
# использование шаблонов
def index(request):
    return render(request, "index.html", context = {"body": "<h1>Hello World!</h1>"})

def about(request):
    header = "Данные пользователя"  # обычная переменная
    langs = ["Python", "Java", "C#"]  # список
    user = {"name": "Tom", "age": 23}  # словарь
    address = ("Абрикосовая", 23, 45)  # кортеж

    data = {"header": header, "langs": langs, "user": user, "address": address}
    return TemplateResponse(request, "about.html", data)


# использование класса TemplateResponse
def contact(request):
    return TemplateResponse(request, "contact.html")

# условие if/else
def ifelse(request):
    data = {"n" : 5}
    return render(request, "ifelse.html", context=data)

# цикл for

def ffoorr(request):
    langs = ["Python", "JavaScript", "Java", "C#", "C++"]
    return render(request, "for.html", context={"langs": langs})

# фильтр дата
def date(request):
    return render(request, "filter.html", context={"my_date": datetime.now()})

