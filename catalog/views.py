from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Contact


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        print(f"{name}({email}): {message}")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено!")
    contact = Contact.objects.get(id=2)
    context = {
        "telephone": contact.telephone,
        "address": contact.address,
        "website": contact.web_site,
    }
    return render(request, "contacts.html", context)
