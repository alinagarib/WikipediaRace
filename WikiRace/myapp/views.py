from django.shortcuts import render, HttpResponse
from .models import Vertex
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.algorithms.graph_algorithms import rand_path, dijkstra_shortest_path

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

def home(request):
    return HttpResponse("hello world")

def graph(request):
    links = Vertex.objects.all()
    return render(request, "graph.html", {"link": links})

@api_view(['GET'])
def get_random_links(request):
    try:
        vertex1, vertex2 = rand_path()
        return Response({
            'start_link': vertex1.link,
            'end_link': vertex2.link
        })
    except ValueError as e:
        return Response({'error': str(e)}, status=400)

@api_view(['POST'])
def get_shortest_path(request):
    start_link = request.data.get('start_link')
    end_link = request.data.get('end_link')

    if not start_link or not end_link:
        return Response({'error': 'Both start_link and end_link are required.'}, status=400)

    try:
        print(f"Calculating shortest path from {start_link} to {end_link}")
        # Check if the vertices exist in the database
        if not Vertex.objects.filter(link__iexact=start_link).exists():
            return Response({'error': f'Start link "{start_link}" not found in the graph.'}, status=404)
        if not Vertex.objects.filter(link__iexact=end_link).exists():
            return Response({'error': f'End link "{end_link}" not found in the graph.'}, status=404)

        # Call the Dijkstra function to find the shortest path
        solution_str = dijkstra_shortest_path(start_link, end_link)
        return Response({'solution': solution_str})
    
    except ValueError as e:
        print(f"Error: {str(e)}")
        return Response({'error': str(e)}, status=400)

    except Exception as e:
        # Log the error for debugging
        print(f"Error during shortest path calculation: {str(e)}")
        return Response({'error': 'An error occurred while calculating the shortest path.'}, status=500)


