from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    context = {'all_pizzas':pizzas}
    return render(request,'pizzas/pizzas.html',context)


def pizza(request,pizza_id):
    p = Pizza.objects.get(id=pizza_id)
    toppings = Topping.objects.filter(pizza=p)
    entries = Entry.objects.filter(pizza=p)
    image = Pizza.image
    context = {'pizza':p, 'toppings':toppings, 'entries': entries, 'image':image}

    return render(request,'pizzas/pizza.html',context)

def new_entry(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST': 
        form = EntryForm()
    else:
        print(request.POST)
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.pizza = pizza
            new_entry.save()
            return redirect('pizzas:pizza',pizza_id=pizza_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/new_entry.html',context)