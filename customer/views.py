from django.shortcuts import render, redirect
from django.views import View
from .models import MenuItem, Category, OrderModel
from django.core.mail import send_mail

# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        
        # get every item from each category/ pega todos os item de cada categoria
        appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')
        entres = MenuItem.objects.filter(category__name__contains='Entre')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')

        # pass into context/ passa para o context

        context = {
            'appetizers': appetizers,
            'entres': entres,
            'desserts': desserts,
            'drinks': drinks,
        }

        # render the template/ carrega o template
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):

        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            price=price,
            name = name,
            email = email,
            city = city,
            street = street,
            state = state,
            zip_code = zip_code,
        )
        order.items.add(*item_ids)

        #depois de tudo feito, evia uma email de confirmação para o usuario
        body = ('Thank you for your order!Your food is being made and will be delivered soon!\n'
        f'Your total:{price}\n'
        'Enjoy your food!')
        send_mail(
            'Thank you for your order!',
            body,
            'example@example.com',
            [email],
            fail_silently =False,
        )

        context = {
            'items': order_items['items'],
            'price': price
        }

        return redirect('order-confirmation', pk=order.pk)

class OrderConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price
        }

        return render(request, 'customer/order_conf.html', context)

    def post(self, request, pk, *args, **kwargs):
        print(request.body)

class OrderPayConfirmation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/order_pay_conf.html')