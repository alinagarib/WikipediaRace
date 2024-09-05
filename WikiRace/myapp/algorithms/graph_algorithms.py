import heapq
import random
from collections import deque
from myapp.models import Vertex, Edge

def dijkstra_shortest_path(start_link, end_link):
    # Initialize the priority queue and distances dictionary
    pq = []
    heapq.heappush(pq, (0, start_link))  # (distance, node)
    distances = {start_link: 0}
    previous_nodes = {start_link: None}
    original_end = end_link

    while pq:
        current_distance, current_link = heapq.heappop(pq)

        if current_link == end_link:
            break

        current_page = Vertex.objects.get(link=current_link)
        links = Edge.objects.filter(from_vertex=current_page)

        for link in links:
            neighbor_link = link.to_vertex.link
            distance = current_distance + 1  # Assume all edges have a weight of 1

            if neighbor_link not in distances or distance < distances[neighbor_link]:
                distances[neighbor_link] = distance
                previous_nodes[neighbor_link] = current_link
                heapq.heappush(pq, (distance, neighbor_link))

    # Reconstruct the shortest path
    path = []
    while end_link is not None:
        path.insert(0, end_link)
        end_link = previous_nodes[end_link]

    solution_str = f"The shortest path from {start_link} to {original_end} can be completed in {distances[path[-1]]} clicks. This is the path: "
    # Concatenate the links in the path to the output string
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
        try:
            dijkstra_shortest_path(vertex1.link, vertex2.link)
            # If the path is found, return the two vertices
            return vertex1, vertex2
        except Exception:
            # If no path exists, select two new random vertices
            continue

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

        # Get all outgoing edges from the current vertex
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

