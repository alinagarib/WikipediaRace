from django.shortcuts import render, HttpResponse
from .models import Vertex

# Create your views here.

def home(request):
    return HttpResponse("hello world")

def graph(request):
    links = Vertex.objects.all()
    return render(request, "graph.html", {"link": links})