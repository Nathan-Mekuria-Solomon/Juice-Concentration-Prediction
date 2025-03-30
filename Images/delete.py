class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dic = {}
        
        for start, end in self.edges:
            if start in self.graph_dic:
                self.graph_dic[start].append(end)
            else:
                self.graph_dic[start] = [end]

    def get_paths(self, start, end, path= []):
        path = path + [start]
        
        if start == end: 
            return path # this whole time I was returning [start] -> big mistake (the graph lost its base case)
        
        if start not in self.graph_dic:
            return []
        
        paths = []
        
        for node in self.graph_dic[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
                    
        return paths
    
    def get_shortest_path(self, start, end, path= []):
        path = path + [start]
        
        if start == end: # recursion base case
            return path
        
        if start not in self.graph_dic: # if the key is not found
            return None
        
        shortest_path = None
        for node in self.graph_dic[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(shortest_path) > len(sp):
                        shortest_path = sp
                        
        return shortest_path
            
if __name__ == '__main__':
    routes = [
        ('Mumbai', "Paris"),
        ('Mumbai', "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "NewYork"),
        ("Dubai", "NewYork"),
        ("NewYork", "Toronto")
    ]
    
    graph = Graph(routes)
    
    start = "Mumbai"
    end = "NewYork"
    
    print(f"shortest path between {start} and {end} is: ", graph.get_shortest_path(start, end))