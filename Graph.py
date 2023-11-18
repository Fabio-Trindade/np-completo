from copy import copy
class Graph:
    def __init__(self, vertex : list, edges:list) -> None:
        self.vertex = vertex
        self.edges = edges
        self.graph = self.generate_graph(vertex,edges)
        self.num_vertex = len(vertex)
        self.num_edges = len(edges)
        pass
    
    def generate_graph(self,vertex:list, edges:list) -> list:
        num_vertex = len(vertex)
        graph = [[0 for j in range(num_vertex)] for i in range(num_vertex)]
        for edge in edges:
            graph[edge[0]][edge[1]] = 1
            graph[edge[1]][edge[0]] = 1
        return graph
    
    def print(self):
        for i in self.graph:
            print(i)
                
    def copy(self):
        return copy(self.graph)
            
            
        