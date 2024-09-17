# Wikipedia Race
This project is a web application that allows users to find the shortest path between two Wikipedia articles. It utilizes the Wikipedia API to scrape articles and build a directed graph representing Wikipedia pages and their hyperlinks. Users can retrieve randomized links from the database or input a starting article and an ending article, and the application calculates the shortest path (in terms of clicks/links) between them.

## Features
Graph Construction: Scrapes Wikipedia starting from a specific page and constructs a graph where vertices represent articles and edges represent hyperlinks.
Breadth-First Search (BFS) Traversal: Efficiently traverses Wikipedia pages up to a specified depth to build the graph.
Shortest Path Calculation: Implements Dijkstra's algorithm to find the shortest path between two articles within the graph.
RESTful API Endpoints: Provides endpoints to interact with the application, including fetching the shortest path and checking if a path exists.
## Technologies Used
- Python & Django: Backend development and web framework.
- Django REST Framework: Building RESTful APIs.
- Requests: Making HTTP requests to the Wikipedia API.
- Getting Started
## Installation
- Clone the Repository
- Create a Virtual Environment
- Install Dependencies
- Apply Migrations
- Run the Scraper
- Start the Development Server
- Usage
## API Endpoints
### Get Shortest Path
- URL: /api/shortest-path/
- Method: POST
- Parameters:
  - start_link (string): Title of the starting Wikipedia article.
  - end_link (string): Title of the ending Wikipedia article.
Description: Calculates the shortest path between the two specified articles.
### Check if Path Exists
- URL: /api/path-exists/
- Method: GET
- Parameters:
  - start_link (string): Title of the starting Wikipedia article.
  - end_link (string): Title of the ending Wikipedia article.
Description: Checks whether a path exists between the two specified articles.

Thank you!

