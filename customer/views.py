from django.shortcuts import render
from django.views import View

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
        aperitivos = MenuItem.objects.filter(category__name__contains='aperitivos')
        bebidas = MenuItem.objects.filter(category__name__contains='bebidas')
        pratoP = MenuItem.objects.filter(category__name__contains='prato principal')
        sobremesa = MenuItem.objects.filter(category__name__contains='sobremesa')
        # pass into context/ passa para o context

        context = {
            'aperitivos': aperitivos,
            'pratoP': pratoP,
            'sobremesa': sobremesa,
            'bebidas': bebidas,
        }

        # render the template/ carrega o template
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        

