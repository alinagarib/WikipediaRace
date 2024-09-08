import heapq
import random
from collections import deque
from myapp.models import Vertex, Edge

def dijkstra_shortest_path(start_link, end_link):
    try:
        start_vertex = Vertex.objects.get(link=start_link)
        end_vertex = Vertex.objects.get(link=end_link)
    except Vertex.DoesNotExist:
        raise ValueError("Start or End link not found in the database.")

    # Priority queue (min-heap) to store the next vertex to process (distance, link)
    pq = []
    heapq.heappush(pq, (0, start_vertex.link))  # (distance, link)
    distances = {start_vertex.link: 0}
    previous_nodes = {start_vertex.link: None}

    while pq:
        current_distance, current_link = heapq.heappop(pq)

        if current_link == end_link:
            break  # Found the shortest path

        # Get current vertex from link
        current_vertex = Vertex.objects.get(link=current_link)

        # Get all outgoing edges (respects directionality)
        outgoing_edges = Edge.objects.filter(from_vertex=current_vertex)

        for edge in outgoing_edges:
            neighbor = edge.to_vertex.link  # Use link instead of the object
            distance = current_distance + 1  # Assuming weight of 1 for all edges

            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_link
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct the shortest path
    path = []
    current = end_link
    while current:
        path.insert(0, current)
        current = previous_nodes.get(current)

    # If no path exists, raise an error or return None
    if path[0] != start_link:
        raise ValueError("No valid path found between the given links.")

    solution_str = f"The shortest path from {start_link} to {end_link} can be completed in {distances[end_link]} clicks. This is the path: "
    solution_str += " -> ".join(path)

    return solution_str


def rand_path():
    # Get all the vertices in the graph
    vertices = list(Vertex.objects.all())

    # Ensure there are at least two vertices to pick from
    if len(vertices) < 2:
        raise ValueError("Not enough vertices in the graph to select two random ones.")

    # Repeat until two vertices with a valid path are found
    while True:
        vertex1, vertex2 = random.sample(vertices, 2)

        # Check if a path exists between vertex1 and vertex2
        if path_exists(vertex1.link, vertex2.link):
            return vertex1, vertex2
        else:
            continue
        # try:
        #     path_exists(vertex1.link, vertex2.link)
        #     # If the path is found, return the two vertices
        #     return vertex1, vertex2
        # except Exception:
        #     # If no path exists, select two new random vertices
        #     continue

def path_exists(start_link, end_link):
    try:
        # Get the start and end vertices from the database
        start_vertex = Vertex.objects.get(link=start_link)
        end_vertex = Vertex.objects.get(link=end_link)
    except Vertex.DoesNotExist:
        # If one of the vertices doesn't exist, return False
        return False

    # If the start and end vertices are the same, return True
    if start_vertex == end_vertex:
        return True

    # Use a queue for BFS
    queue = deque([start_vertex])
    visited = set([start_vertex])  # To track visited vertices

    # Perform BFS to find the path
    while queue:
        current_vertex = queue.popleft()

        # Get all outgoing edges from the current vertex (respect directionality)
        edges = Edge.objects.filter(from_vertex=current_vertex)

        for edge in edges:
            neighbor = edge.to_vertex

            if neighbor == end_vertex:
                # If we reached the destination vertex, return True
                return True

            if neighbor not in visited:
                # Add the neighbor to the queue and mark it as visited
                queue.append(neighbor)
                visited.add(neighbor)

    # If BFS completes and we haven't found the end vertex, return False
    return False


