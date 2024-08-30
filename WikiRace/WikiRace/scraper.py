import requests
# from graph import Graph
import time
from collections import deque
import os
import django
import sys

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WikiRace.settings')
django.setup()

# from WikiRace.WikiApp.models import Vertex, Edge
from WikiRace.graph import Graph

def getWikiLinks(title):
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "titles": f'{title}',
        "prop": "links",
        "pllimit": "max"
    }

    links = []

    while True:
        response = S.get(url=URL, params=PARAMS)
        data = response.json()
        
        pages = data['query']['pages'] # Response contains dict of pages

        # Gets link titles from page and appends links array
        for page_id in pages:
            if 'links' in pages[page_id]:
                for link in pages[page_id]['links']:
                    if ':' not in link['title']: # Check to exclued special links
                        links.append(link['title'])

        # Check for continuation key, allows to check accross multiple pages
        if 'continue' in data:
            PARAMS.update(data['continue'])
        else:
            break

        time.sleep(0.5)

    return links

# def populateGraph(title, g):
#     # Gets all links from a given page

#     neighbors = getWikiLinks(title)
#     g.addVertex(title) # Adds vertex into the graph

#     for link in neighbors: # Adds all neighbors into the vertex
#         # g.vertices[title].addNeighbor(link)
#         g.addEdge(title, link) # Created edges in the graph from the passed in page to each neighbor

#     for link in neighbors:
#         neighbors = getWikiLinks(link)
#         g.addVertex(link)
#         for edge in neighbors:
#             # g.vertices[link].addNeighbor(edge)
#             g.addEdge(link, edge)

def populateBFS(start, g, max=5):
    queue = deque([(start, 0)])  # Queue to manage BFS, store (link, depth)
    visited = set()  # Set to track visited pages and avoid re-fetching

    while queue:
        current_link, depth = queue.popleft()

        if depth > max:
            continue

        if current_link not in visited:
            visited.add(current_link)
            neighbors = getWikiLinks(current_link)
            # print(f"Neighbors of {current_link}: {neighbors}")
            g.addVertex(current_link)

            for link in neighbors:
                g.addEdge(current_link, link)
                if link not in visited:
                    queue.append((link, depth + 1))


if __name__ == "__main__": 
    links = Graph()
    populateBFS("Main Page", links)