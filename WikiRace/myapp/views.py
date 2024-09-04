from django.shortcuts import render, HttpResponse
from .models import Vertex

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import Vertex, Edge

@api_view(['GET'])
def get_graph_data(request):
    vertices = Vertex.objects.all()
    edges = Edge.objects.all()

    nodes = [{'id': vertex.link} for vertex in vertices]
    links = [{'source': edge.from_vertex.link, 'target': edge.to_vertex.link} for edge in edges]

    graph_data = {
        'nodes': nodes,
        'links': links
    }

    return Response(graph_data)

# def home(request):
#     return HttpResponse("hello world")

# def graph(request):
#     links = Vertex.objects.all()
#     return render(request, "graph.html", {"link": links})
