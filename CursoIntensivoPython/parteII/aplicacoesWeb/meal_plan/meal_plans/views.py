from django.shortcuts import render

# Create your views here.
def index(request):
    """A pagina inicial"""
    return render(request,'meal_plans/index.html')