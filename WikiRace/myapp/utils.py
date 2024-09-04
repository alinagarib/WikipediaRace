# from vertex import Vertex
from myapp.models import Vertex, Edge

# Each link between a page is a directed edge
# class Graph:

#     def __init__(self):
#         self.vertices = {} # Dict to store all vertices
        
    
#     def addVertex(self, link):
#         if link not in self.vertices: # checks if vertice already exists in the graph
#             # Creates new vertex with passed in link
#             self.vertices[link] = Vertex(link)
#         return self.vertices[link]
        
#     def addEdge(self, from_link, to_link):
#         # Checks if the passed in links exist as vertices

#         if from_link not in self.vertices:
#             self.addVertex(from_link)
#         if to_link not in self.vertices:
#             self.addVertex(to_link)

#         from_vertex = self.vertices[from_link]
#         to_vertex = self.vertices[to_link]

#         from_vertex.addNeighbor(to_vertex) 

#     def getVertex(self, link):
#         return self.vertices.get(link)  # Return the Vertex object for the given link, if it exists
    
#     def getVertices(self):
#         return self.vertices.keys()  # Return all the links in the graph
    
#     def __iter__(self):
#         return iter(self.vertices.values()) # Creates an iterable so that the values of a vertice can be iterated over
    
#     # def __str__(self):
#     #     result = ""
#     #     for link in self.vertices:
#     #         result += str(self.vertices[link]) + "\n"
#     #     return result
class Graph:

    def addVertex(self, link):
        vertex, created = Vertex.objects.get_or_create(link=link)
        return vertex

    def addEdge(self, from_link, to_link):
        if from_link not in self.getVertices():
            from_vertex = self.addVertex(from_link)
        if to_link not in self.getVertices():
            to_vertex = self.addVertex(to_link)

        Edge.objects.get_or_create(from_vertex=from_vertex, to_vertex=to_vertex)

    def getVertex(self, link):
        return Vertex.objects.get(link=link)

    def getVertices(self):
        return Vertex.objects.all()
