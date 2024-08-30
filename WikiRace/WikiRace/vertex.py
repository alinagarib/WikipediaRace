# Each page is a vertex
# class Vertex:
#     def __init__(self, link):
#         self.link = link
#         self.adj = [] # list for all outgoing links of a link
    
#     def addNeighbor(self, neighbor):
#         if neighbor not in self.adj: # checks if link is already a neighbor of a link, if not appends the dict
#             self.adj.append(neighbor)

#     def getLink(self):
#         return self.link
    
#     def getNeighbors(self):
#         return self.adj
    
    # def __str__(self):
    #     result = self.link + " points to "

    #     neighbors_arr = []

    #     # Loop through each neighbor in the neighbors list
    #     for neighbor in self.adj:
    #         # Access the link of the neighbor and add it to the neighbor_links list
    #         neighbors_arr.append(neighbor.link)

    #     # Join the list of neighbor links into a single string, separated by commas
    #     neighbors_str = ', '.join(neighbors_arr)

    #     # Add the neighbors string to the result
    #     result += "[" + neighbors_str + "]"

    #     return result
    
    
