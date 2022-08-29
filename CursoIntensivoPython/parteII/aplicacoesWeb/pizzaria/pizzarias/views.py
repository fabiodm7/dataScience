from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    return render(request,'pizzarias/index.html')

def menu(request):
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas':pizzas}
    return render(request,'pizzarias/menu.html',context)

def sabor(request,sabor_id):
    pizza = Pizza.objects.get(id=sabor_id)
    toppings = pizza.topping_set.all
    context = {'pizza':pizza,'toppings':toppings}
    return render(request,'pizzarias/sabor.html',context)