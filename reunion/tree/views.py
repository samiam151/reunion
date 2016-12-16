from django.shortcuts import render

# Create your views here.
def tree_home(request):
    return render(request, 'tree/index.html', {})