"""
URL configuration for lessons project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from lessonone import views



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='home'),
# ]


# Чтобы эти функции сопоставлялись с запросами, надо определить для них маршруты в проекте в файле urls.py



urlpatterns = [
    #получение информации о запросе
    path('index', views.index),
    # Ее преимущесто состоит в том, что она
    # позволяет задать адреса URL с помощью регулярных выражений. (функция re_path)
    # re_path(r'^about', views.about),
    # path('contact', views.contact),
    # использование kwargs
    # path('about', views.about, kwargs={"name":"Tom", "age": 38}),
#     Определение параметров через функцию path
    path("user/<str:name>", views.user),
    # переадресация
    path("details/", views.details),
    # использование шаблонов
    path("", views.index),
    path("about/", views.about),
    path("contact/", views.contact),
    path("ifelse/", views.ifelse),
    path("ffoorr/", views.ffoorr),
    path("date/", views.date),


]
