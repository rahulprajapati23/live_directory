from itertools import permutations

INF = float('inf')

cost = [
    [INF, 20, 30, 10, 11],
    [15, INF, 16, 4, 2],
    [3, 5, INF, 2, 4],
    [19, 6, 18, INF, 3],
    [16, 4, 7, 16, INF]
]

n = len(cost)
cities = range(n)

min_cost = INF
best_path = None

start = 0 
for perm in permutations([i for i in cities if i != start]):
    path = [start] + list(perm) + [start]
    total = 0
    valid = True
    
    for i in range(len(path) - 1):
        c = cost[path[i]][path[i+1]]
        if c == INF:
            valid = False
            break
        total += c
    
    if valid and total < min_cost:
        min_cost = total
        best_path = path

print("Minimum Path")
for i in range(len(best_path) - 1):
    print(f"{best_path[i] + 1} – {best_path[i+1] + 1} = {cost[best_path[i]][best_path[i+1]]}")

print(f"\nMinimum cost: {min_cost}")

print("Path Taken:", " - ".join(str(x+1) for x in best_path))
