# from SPARQLWrapper import SPARQLWrapper, JSON


# def getWikiLinks(title):
#     headers = {
#         'User-Agent': 'WikiRaceScraper/1.0 (mailto:alinagrb@gmail.com)',
#         'Accept': 'application/sparql-results+json',
#     }

#     query = f"""
#     SELECT ?linkedItemLabel WHERE {{
#       ?wikiTitle schema:name "{title}"@en .
#       ?wikiTitle schema:about ?wikidataEntity .

#       ?wikidataEntity ?property ?linkedItem .

#       FILTER(isIRI(?linkedItem)).
#       ?linkedItem rdfs:label ?linkedItemLabel .
#       FILTER(LANG(?linkedItemLabel) = "en").
#       FILTER(!regex(?linkedItemLabel, "^[0-9]+$")).

#       SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" . }}
#     }}
#     """

#     url = 'https://query.wikidata.org/sparql'
#     params = {'query': query}

#     response = requests.get(url, headers=headers, params=params)

#     if response.status_code != 200:
#         raise Exception(f"Query failed with status code {response.status_code}: {response.text}")

#     results = response.json()

#     links = []
#     for result in results["results"]["bindings"]:
#         link_label = result["linkedItemLabel"]["value"].strip()
#         links.append(link_label)

#     return links


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

# if __name__ == "__main__": 
#     links = Graph()
#     populateBFS("Main Page", links)