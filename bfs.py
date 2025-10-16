from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph using adjacency list
graph = {
    0: [1, 2, 3],
    1: [0],
    2: [0, 4],
    3: [0, 5],
    4: [2, 6, 7],
    5: [3],
    6: [4], 7: [4]
}

print("BFS Traversal:")
bfs(graph, 0)
