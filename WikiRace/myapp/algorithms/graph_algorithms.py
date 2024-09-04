import heapq
from myapp.models import Vertex, Edge

def dijkstra_shortest_path(start_title, end_title):
    # Initialize the priority queue and distances dictionary
    pq = []
    heapq.heappush(pq, (0, start_title))  # (distance, node)
    distances = {start_title: 0}
    previous_nodes = {start_title: None}

    while pq:
        current_distance, current_title = heapq.heappop(pq)

        if current_title == end_title:
            break

        current_page = Vertex.objects.get(title=current_title)
        links = Edge.objects.filter(source=current_page)

        for link in links:
            neighbor_title = link.target.title
            distance = current_distance + 1  # Assume all edges have a weight of 1

            if neighbor_title not in distances or distance < distances[neighbor_title]:
                distances[neighbor_title] = distance
                previous_nodes[neighbor_title] = current_title
                heapq.heappush(pq, (distance, neighbor_title))

    # Reconstruct the shortest path
    path = []
    while end_title is not None:
        path.insert(0, end_title)
        end_title = previous_nodes[end_title]

    return path, distances[path[-1]]

def rand_paths():
    pass