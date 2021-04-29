from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    # the home page for pizzeria
    return render(request, "Pizza/index.html")


def pizzas(request):
    pizzas = Pizza.objects.order_by("date_added")

    context = {"pizzas": pizzas}
    return render(request, "Pizza/pizzas.html", context)
