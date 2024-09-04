from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("graph/", views.graph, name="graph"),
    path('api/graph/', views.get_graph_data, name='graph-data'),
]