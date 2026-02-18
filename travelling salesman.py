import heapq

# Graph input
graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input("Enter neighbors with cost (format: node,cost): ").split()
    
    graph[node] = {}
    for item in neighbors:
        if item:
            neighbor, cost = item.split(',')
            graph[node][neighbor] = int(cost)

# Heuristic input
print("\nEnter heuristic values:")
for node in graph:
    h = int(input(f"Heuristic of {node}: "))
    heuristic[node] = h

start = input("Enter start node: ")
goal = input("Enter goal node: ")

def astar(graph, heuristic, start, goal):
    open_list = [(0, start)]
    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor in graph[current]:
            cost = g_cost[current] + graph[current][neighbor]

            if neighbor not in g_cost or cost < g_cost[neighbor]:
                g_cost[neighbor] = cost
                priority = cost + heuristic[neighbor]
                heapq.heappush(open_list, (priority, neighbor))
                parent[neighbor] = current

    return None


path = astar(graph, heuristic, start, goal)

print("\nShortest Path:", path)
