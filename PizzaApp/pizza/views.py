from django.shortcuts import render
from django.http import HttpResponse
from .models import topping
from .models import pizza
from django.shortcuts import get_object_or_404, render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def chef(request):
    pizzas = pizza.objects.all()
    toppings = topping.objects.all()
    context = { 'pizza': pizzas, 'topping': toppings }
    return render(request, 'pizza/pizzaChef.html', context)
def owner(request):
    toppings = topping.objects.all()
    context = { 'topping': toppings }
    return render(request, 'pizza/index.html', context)

def addtopping(request, name):
    duplicateFound = topping.objects.filter(topping_name=name).exists()
    if(not duplicateFound):
        toppings = topping.objects.all().order_by('-topping_ID')
        theid = 0
        if(toppings):
            thetopping = toppings[0]
            theid = int(thetopping.topping_ID) + 1
        newtopping = topping.objects.create(topping_name = name, topping_ID = str(theid))
        return HttpResponse("topping added!")

def remtopping(request, name):
    remtopping =topping.objects.get(topping_ID =name)
    remtopping.delete()
    return HttpResponse("topping removed!")
    
def updtopping(request, select, name):
    if(name):
        updtopping =topping.objects.get(topping_ID =select)
        updtopping.topping_name = name
        updtopping.save()
        return HttpResponse("topping changed!")

def addpizza(request, name, toppings):
    duplicateFound = pizza.objects.filter(pizza_name=name).exists()
    if(not duplicateFound):
        pizzas = pizza.objects.all().order_by('-pizza_ID')
        theid = 0
        if(pizzas):
            thepizza = pizzas[0]
            theid = int(thepizza.pizza_ID) + 1
        pizzas = pizza.objects.create(pizza_name = name, pizza_ID = str(theid), pizza_topping = toppings)
        return HttpResponse("pizza added!")

def rempizza(request, name):
    rempizza =pizza.objects.get(pizza_ID =name)
    rempizza.delete()
    return HttpResponse("pizza removed!")
    
def updpizza(request, select, name, toppings):
    if(name):
        updpizza = pizza.objects.get(pizza_ID = select)
        if(not name=="invalid"):
            updpizza.pizza_name = name

        updpizza.pizza_topping = ""
        if(not toppings=="invalid"):
            updpizza.pizza_topping = toppings

        updpizza.save()
        return HttpResponse("pizza changed!")
# Create your views here.

#def detail(request, question_id):
   # question = get_object_or_404(Question, pk=question_id)
  #  return render(request, 'polls/detail.html', {'question': question})