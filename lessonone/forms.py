from django import forms


class UserForm(forms.Form):

    #  label позволяет установить текстовую метку, которая отображается рядом с полем
    #  Параметр help_text устанавливает подсказку рядом с полем ввода
    name = forms.CharField(label="Имя", help_text="Введите свое имя")
    age = forms.IntegerField(label="Возраст", help_text="Введите свой возраст")