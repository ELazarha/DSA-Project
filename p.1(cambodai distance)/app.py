from collections import defaultdict, deque


class Graph:

    graph = defaultdict(list)

    def __init__(self, graph):
        self.graph = graph

    # add edge
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    # generate edges
    def generate_edges(self):
        edges = []
        for node in self.graph:
            for neighbour in self.graph[node]:
                edges.append((node, neighbour))
        return edges

    # generate list
    def generate_adjacency_list(self):
        for node in self.graph:
            print(node, end=" -> ")
            neighbours = self.graph[node]
            for i, neighbour in enumerate(neighbours):
                if i == len(neighbours) - 1:
                    print(neighbour, end="")
                else:
                    print(neighbour, end=" -> ")
            print()

    # i want function start from 1 to 2

    def dijkstra(self, start):
        visited = []
        distances = {node: float("inf") for node in self.graph}
        distances[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                for neighbour, weight in self.graph[node]:
                    if distances[neighbour] > distances[node] + weight:
                        distances[neighbour] = distances[node] + weight
                        queue.append(neighbour)

        return distances

    def target(self, start, target):
        visited = []
        distances = {node: float("inf") for node in self.graph}
        distances[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                for neighbour, weight in self.graph[node]:
                    if distances[neighbour] > distances[node] + weight:
                        distances[neighbour] = distances[node] + weight
                        queue.append(neighbour)
        return distances[target]


# create the graph given in above figure
g = Graph()

g.add_edge("pnhom penh", "siem reap", 3)
g.add_edge("siem reap", "sihanoukville", 5)
g.add_edge("siem reap", "kampot", 2)

g.add_edge("pnhom penh", "ompenh", 1)
g.add_edge("pnhom penh", "siem reap", 100)
g.add_edge("siem reap", "ompenh", 1)


g.generate_adjacency_list()

sortpath = g.target("pnhom penh", "sihanoukville" )

print(f"shortest path from pnhom penh to sihanoukville is {sortpath}")
