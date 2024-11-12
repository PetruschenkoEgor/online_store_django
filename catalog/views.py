from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Contact, Product, Category


def home(request):
    """Главная страница"""
    # products = Product.objects.all()[2:5]
    # context = {"products": products}
    # for product in context.get("products"):
    #     print(f"Наименование товара - {product.name}")
    #     print(f"Цена товара - {product.price}")
    #     print(f"Описание товара - {product.description}")
    #     print()
    products_list = []
    for count in range(1, 4):
        product = Product.objects.get(id=count)
        products_list.append(product)
        print(f"Наименование товара - {product.name}")
        print(f"Цена товара - {product.price}")
        print(f"Описание товара - {product.description}")
        print()
    context = {"products": products_list}
    return render(request, "home.html", context)


def contacts(request):
    """Страница с контактами"""
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


def product_page(request, pk):
    """Страница с информацией о продукте"""
    # Либо найдется страница, либо выскочит ошибка 404
    prod = get_object_or_404(Product, pk=pk)
    context = {"product": prod}
    return render(request, "product.html", context)


def add_product(request):
    """Страница добавления продукта"""
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.POST.get("image")
        category_id = request.POST.get("category")
        price = request.POST.get("price")
        # Получаем категорию
        category = get_object_or_404(Category, pk=category_id)
        # Создаем продукт и сохраняем его в БД
        product = Product(
            name=name,
            description=description,
            image=image,
            category=category,
            price=price,
        )
        product.save()
        return HttpResponse("Продукт успешно добавлен!")
    return render(request, "add_product.html")
