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

# Input heuristic values
heuristic = {}
print("Enter heuristic values h(n):")
for i in range(n):
    heuristic[i] = int(input(f"h({i}) = "))

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))

def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start))  
    # (f = g + h, g, node)

    visited = set()

    while open_list:
        f, g, node = heapq.heappop(open_list)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Goal reached!")
            return g

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor))

    return float("inf")

result = astar(start, goal)

if result != float("inf"):
    print("Minimum cost from", start, "to", goal, "is:", result)
else:
    print("Goal not reachable")
