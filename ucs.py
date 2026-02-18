import heapq

# Input number of vertices and edges
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

# Adjacency list: node -> (neighbor, cost)
graph = {i: [] for i in range(n)}

print("Enter edges (u v cost):")
for _ in range(e):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))   # remove for directed graph

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))

def ucs(start, goal):
    priority_queue = [(0, start)]   # (cost, node)
    visited = set()

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Goal reached!")
            return cost

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor))

    return float("inf")

result = ucs(start, goal)

if result != float("inf"):
    print("Minimum cost from", start, "to", goal, "is:", result)
else:
    print("Goal not reachable")
