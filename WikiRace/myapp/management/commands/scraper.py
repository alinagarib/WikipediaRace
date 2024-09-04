import requests
# from graph import Graph
import time
from collections import deque
import os
import django
import sys
from django.core.management.base import BaseCommand

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WikiRace.settings')
django.setup()

# from WikiRace.WikiApp.models import Vertex, Edge
from myapp.utils import Graph
from myapp.models import Vertex, Edge



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

        time.sleep(0.1)

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

def populateBFS(start, g, max=1):
    queue = deque([(start, 0)])  # Queue to manage BFS, store (link, depth)
    visited = set()  # Set to track visited pages and avoid re-fetching

    while queue:
        current_link, depth = queue.popleft()

        if depth > max:
            continue

        if current_link not in visited:
            visited.add(current_link)
            neighbors = getWikiLinks(current_link)
             # Save the current vertex to the database
            from_vertex, created = Vertex.objects.get_or_create(link=current_link)
            print(f"Neighbors of {current_link}: {neighbors}")
            g.addVertex(current_link)

            for link in neighbors:
                to_vertex, created = Vertex.objects.get_or_create(link=link)
                Edge.objects.get_or_create(from_vertex=from_vertex, to_vertex=to_vertex)
                g.addEdge(current_link, link)
                if link not in visited:
                    queue.append((link, depth + 1))


# if __name__ == "__main__": 
#     links = Graph()
#     populateBFS("Main Page", links)

class Command(BaseCommand):
    help = 'Scrape Wikipedia starting from the "Main Page" with a depth of 1 by default, and populate the graph in the database.'

    def add_arguments(self, parser):
        parser.add_argument('--start_page', type=str, default='Main Page', help='The title of the Wikipedia page to start scraping from (default: "Main Page").')
        parser.add_argument('--max_depth', type=int, default=1, help='The maximum depth to traverse from the start page (default: 1).')

    def handle(self, *args, **kwargs):
        start_page = kwargs.get('start_page', 'Main Page')
        max_depth = kwargs.get('max_depth', 1)
        
        self.stdout.write(f"Starting to scrape from {start_page} with a max depth of {max_depth}...")
        
        # Create the Graph instance
        graph = Graph()

        # Call the populateBFS function
        populateBFS(start_page, graph, max_depth)
        
        self.stdout.write(self.style.SUCCESS(f"Scraping complete from {start_page} with max depth {max_depth}."))

# usage : python manage.py scraper
# or : python manage.py scraper --start_page="Albert Einstein" --max_depth=3
