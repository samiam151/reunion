from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

# Family Tree
def family_tree(request):
    return render(request, 'home/tree.html')