def dijkstra(graph, start):
    n = len(graph)
    visited = [False] * n
    dist = [float('inf')] * n
    dist[start] = 0

    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        
        visited[u] = True
        
        for v in range(n):
            if graph[u][v] != float('inf') and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    return dist

nodes = ["A", "B", "C", "D", "E"]
graph = [
    [0, 20, 30, float('inf'), float('inf')],
    [float('inf'), 0, float('inf'), 15, float('inf')],
    [float('inf'), float('inf'), 0, float('inf'), 25],
    [float('inf'), float('inf'), float('inf'), 0, 10],
    [float('inf'), float('inf'), float('inf'), float('inf'), 0]
]

start_node = "A"
start_index = nodes.index(start_node)

distances = dijkstra(graph, start_index)

print("Source → Destination → Cost")
for i, d in enumerate(distances):
    print(f"{start_node} → {nodes[i]} = {d}")
