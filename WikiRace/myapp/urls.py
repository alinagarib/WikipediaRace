from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("graph/", views.graph, name="graph"),
    path('api/graph/', views.get_graph_data, name='graph-data'),
    path('api/random-links/', views.get_random_links, name='get-random-links'),
    path('api/shortest-path/', views.get_shortest_path, name='get-shortest-path'),
]