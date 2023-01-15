from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Recipe
# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/pages/home.html', context)
    
def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
            ).order_by('-id')
    )
    
    context = {
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | ',
    }
    return render(request, 'recipes/pages/category.html', context)

def recipe(request, id):
    recipe = get_object_or_404(
        Recipe,
        pk=id,
        is_published=True
    )
    
    context = {
        'recipe': recipe,
        'is_detail_page': True,
    }
    return render(request, 'recipes/pages/recipe-view.html', context)