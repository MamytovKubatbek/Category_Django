from django.shortcuts import render
from .models import *
# Create your views here.

def main(request):
    category = Category.objects.all()
    meals = Meals.objects.all()
    context = {
        'meals': meals, 
        'category': category,
    
    }
    return render(request, 'index.html', context=context)


