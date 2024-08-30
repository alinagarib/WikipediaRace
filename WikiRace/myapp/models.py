from django.db import models

# Create your models here.

class Vertex(models.Model):
    link = models.CharField(max_length=255, unique=True)

    def add_neighbor(self, neighbor):
        if not self.neighbors.filter(id=neighbor.id).exists():
            self.neighbors.add(neighbor)

    def get_neighbors(self):
        return self.neighbors.all()

    # def __str__(self):
    #     return self.link

class Edge(models.Model):
    from_vertex = models.ForeignKey(Vertex, related_name='outgoing_edges', on_delete=models.CASCADE)
    to_vertex = models.ForeignKey(Vertex, related_name='incoming_edges', on_delete=models.CASCADE)

