from django.shortcuts import render, get_object_or_404
from .forms import UserForm, ProductForm
from .models import User, Order, Product
from datetime import datetime, timedelta


def index(request):
    # products = Product.objects.all()
    context = {'title': 'Main',
               'h1': 'Главная страница сайта',
               'h2': 'Сайт сделан на Django',
               # 'products': products,
               }
    return render(request, 'myapp/index.html', context)


def about(request):
    context = {'title': 'About me',
               'fio': 'Иванов Иван Ивановчи',
               'phone': '+7(999) 999-99-99',
               'adress': 'г Москва, ул. Тверская 1'
               }
    return render(request, 'myapp/about.html', context)


def orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer_id=user_id)
    context = {"user": user, "orders": orders, "title": "Все заказы пользователя"}
    return render(request, 'myapp/orders.html', context)


def order_last_days(request, user_id):
    days = [7, 30, 365]
    result = {}
    user = User.objects.filter(pk=user_id).first()
    for day in days:
        last_day = datetime.now() - timedelta(days=day)
        orders = Order.objects.filter(customer_id=user, date_ordered__gte=last_day)
        products = set()
        for order in orders:
            for product in order.products.all():
                products.add(product)
        result[day] = products
    context = {"7days": result[7],
               "30days": result[30],
               "365days": result[365],
               "title": "Товары за 7, 30, 365 дней",
               "user": user,
               }
    return render(request, 'myapp/orders_last_days.html', context)


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            user = User(username=username,
                        email=email,
                        phone=phone,
                        address=address,
                        )
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Введите данные'
    return render(request, 'myapp/add_user_form.html', {'form': form, 'message': message})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            rating = form.cleaned_data['rating']
            image = form.cleaned_data['image']
            product = Product(name=name,
                              category=category,
                              description=description,
                              price=price,
                              quantity=quantity,
                              rating=rating,
                              image=image,
                              )
            product.save()
            message = 'Товар сохранён'
    else:
        form = ProductForm()
        message = 'Введите данные товара'
    return render(request, 'myapp/add_product_form.html', {'form': form, 'message': message})
