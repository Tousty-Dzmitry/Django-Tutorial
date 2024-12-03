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

from .forms import UserForm


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

# формы для получения данных

def formindex(request):
    return render(request, "formindex.html")


def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")


# джанго формы

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}</h2>")
    else:
        userform = UserForm()
        return render(request, "form.html", {"form": userform})


#  четыре представления для получения, сохранения, редактирования и удаления данных

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person


# получение данных из бд
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

