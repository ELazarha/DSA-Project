from collections import defaultdict, deque
from typing import Dict, List, Tuple
from tabulate import tabulate


class Graph:
    def __init__(self):
        self.graph: Dict[str, List[Tuple[str, int]]] = defaultdict(list)

    def add_edge(self, u: str, v: str, w: int):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def generate_edges(self) -> List[Tuple[str, Tuple[str, int]]]:
        edges = []
        for node in self.graph:
            for neighbour in self.graph[node]:
                edges.append((node, neighbour))
        return edges

    def generate_adjacency_list(self):
        for node in self.graph:
            neighbours = self.graph[node]
            neighbours_str = " -> ".join(
                f"{neighbour} ({weight})" for neighbour, weight in neighbours
            )
            print("--------------------")
            print(f"{node} -> {neighbours_str}")

    def dijkstra(self, start: str) -> Tuple[Dict[str, float], Dict[str, str]]:
        visited = []
        distances = {node: float("inf") for node in self.graph}
        previous_nodes = {node: None for node in self.graph}
        distances[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                for neighbour, weight in self.graph[node]:
                    if distances[neighbour] > distances[node] + weight:
                        distances[neighbour] = distances[node] + weight
                        previous_nodes[neighbour] = node
                        queue.append(neighbour)

        return distances, previous_nodes

    def print_dijkstra_result(self, start: str):
        distances, previous_nodes = self.dijkstra(start)
        print(f"Distances from {start}:")
        for node, distance in distances.items():
            print(f"  {node}: {distance}")

    def target(self, start: str, target: str) -> float:
        distances, _ = self.dijkstra(start)
        return distances[target]

    def shortest_path(self, start: str, target: str):
        distances, previous_nodes = self.dijkstra(start)
        path = []
        current_node = target

        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes[current_node]

        path = path[::-1]  # Reverse the path to get it from start to target

        print(f"Shortest path from {start} to {target}: {' -> '.join(path)}")
        print(f"Total distance: {distances[target]}")


# Create the graph
g = Graph()

edges = [
    ("oddar meanchey", "siem reap", 129),
    ("oddar meanchey", "preah vihear", 164),
    ("oddar meanchey", "banteay meanchey", 127),
    ("preah vihear", "siem reap", 207),
    ("preah vihear", "stung treng", 181),
    ("preah vihear", "kampong thom", 263),
    ("siem reap", "banteay meanchey", 124),
    ("siem reap", "kampong thom", 188),
    ("siem reap", "battambang", 163),
    ("banteay meanchey", "battambang", 105),
    ("pailin", "battambang", 79),
    ("battambang", "pursat", 162),
    ("battambang", "kampong chhnang", 238),
    ("pursat", "koh kong", 246),
    ("pursat", "preah vihear", 380),
    ("pursat", "kampong chhnang", 137),
    ("pursat", "kampong speu", 149),
    ("kampong chhnang", "phnom penh", 101),
    ("kampong chhnang", "kampong thom", 138),
    ("kampong chhnang", "kampong cham", 145),
    ("kampong speu", "koh kong", 259),
    ("kampong speu", "phnom penh", 77),
    ("kampong speu", "takeo", 115),
    ("kampong speu", "kampot", 129),
    ("koh kong", "sihanoukville", 209),
    ("koh kong", "kampot", 257),
    ("sihanoukville", "kampot", 103),
    ("kampot", "takeo", 90),
    ("kampot", "kep", 23),
    ("takeo", "kandal", 83),
    ("kep", "takeo", 91),
    ("phnom penh", "kampong cham", 107),
    ("phnom penh", "prey veng", 91),
    ("phnom penh", "kandal", 36),
    ("kandal", "svay rieng", 170),
    ("kandal", "prey veng", 130),
    ("kampong thom", "preah vihear", 193),
    ("kampong thom", "kratie", 195),
    ("kampong thom", "stung treng", 289),
    ("stung treng", "kratie", 135),
    ("stung treng", "ratanakiri", 181),
    ("stung treng", "mondulkiri", 146),
    ("ratanakiri", "mondulkiri", 119),
    ("mondulkiri", "kratie", 208),
    ("kratie", "kampong cham", 122),
    ("kratie", "kampong thom", 195),
    ("kampong cham", "phnom penh", 107),
    ("prey veng", "svay rieng", 93),
    ("prey veng", "kandal", 124),
    ("svay rieng", "prey veng", 63),
]

for u, v, w in edges:
    g.add_edge(u, v, w)


def main():
    while True:
        print("\nMenu:")
        print("1. Display adjacency list")
        print("2. Find shortest path")
        print("3. Find shortest path from a province")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            g.generate_adjacency_list()
        elif choice == "2":
            start = input("Enter the your province: ")
            target = input("Enter the target province: ")
            if start not in g.graph or target not in g.graph:
                print("Invalid province. Please try again.")
                continue
            g.shortest_path(start, target)
        elif choice == "3":
            province = input("Enter the province: ")
            if province not in g.graph not in g.graph:
                print("Invalid province. Please try again.")
                continue
            else:
                print(g.print_dijkstra_result(province))

        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
