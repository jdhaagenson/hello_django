from django.shortcuts import render

# Create your views here.


def index_view(request):
    message = 'Hello Django!'
    return render(request, 'index.html', {'message':message})