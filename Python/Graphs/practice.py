from collections import defaultdict

class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = defaultdict(list)
        #Start,End is used to uncompact a tupple
        for start,end in self.edges:
            self.graph_dict[start].append(end)

    def get_paths(self,start,end,path=[]):
        path += [start]
        if start == end:
            return [path]
        if start not in self.graph_dict.keys():
            return
        for destination in self.graph_dict[start]:
            path += [self.get_paths(destination, end)]
        return path
        

if __name__ == "__main__":
    routes = [
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("New York","Toronto")
    ]

    route_graph = Graph(routes)
    print(route_graph.graph_dict.items())

    start = "Mumbai"
    end = "Toronto"

    print(f"The paths between {start} and {end} are {route_graph.get_paths(start,end)}")