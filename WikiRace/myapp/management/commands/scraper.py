import requests
# from graph import Graph
import time
from collections import deque
import os
import django
import sys
from django.core.management.base import BaseCommand
#import urllib

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WikiRace.settings')
django.setup()

# from WikiRace.WikiApp.models import Vertex, Edge
from myapp.utils import Graph
from myapp.models import Vertex, Edge

# API request implememnation
def getWikiLinks(title):
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    # First, resolve redirects to get the actual page title
    PARAMS = {
        "action": "query",
        "format": "json",
        "titles": title,
        "redirects": 1
    }

    response = S.get(url=URL, params=PARAMS)
    data = response.json()

    # Get the normalized title after redirects
    pages = data['query']['pages']
    page_id = next(iter(pages))
    resolved_title = pages[page_id]['title']

    # Now use action=parse to get all links, including those from templates
    PARAMS = {
        "action": "parse",
        "format": "json",
        "page": resolved_title,
        "prop": "links",
        "pllimit": "max",
        "redirects": 1
    }

    response = S.get(url=URL, params=PARAMS)
    data = response.json()

    links = []

    if 'parse' in data and 'links' in data['parse']:
        for link in data['parse']['links']:
            link_title = link['*'].strip()
            # Exclude special pages and files
            if ':' not in link_title and not link_title.isnumeric():
                links.append(link_title)

    return links


def populateBFS(start, g, max):
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
            time.sleep(0.1)
            from_vertex, created = Vertex.objects.get_or_create(link=current_link)
            # print(f"Neighbors of {current_link}: {neighbors}")
            g.addVertex(current_link)

            for link in neighbors:
                to_vertex, created = Vertex.objects.get_or_create(link=link)
                Edge.objects.get_or_create(from_vertex=from_vertex, to_vertex=to_vertex)
                g.addEdge(current_link, link)
                if link not in visited:
                    queue.append((link, depth + 1))


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
