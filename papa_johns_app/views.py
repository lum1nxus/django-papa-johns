from django.shortcuts import render, redirect
from .forms import PizzaOrderForm
from .models import PizzaOrder


def home(request):
    return render(request, 'home.html')


def place_order(request):
    if request.method == 'POST':
        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            pizza_type = form.cleaned_data['pizza_type']
            comments = form.cleaned_data['comments']

            PizzaOrder.objects.create(
                pizza_type=pizza_type,
                comments=comments
            )
            return redirect('/orders')

    else:
        form = PizzaOrderForm()
    return render(request, 'place_order.html', {'form': form})


def orders_table(request):
    orders = PizzaOrder.objects.all()
    return render(request, 'orders_table.html', {'orders': orders})