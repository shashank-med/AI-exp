import heapq

def uniform_cost_search(graph, start, goal):
    queue = []
    heapq.heappush(queue, (0, start, [start]))

    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node == goal:
            return cost, path

        if node not in visited:
            visited.add(node)

            for next_node, weight in graph[node]:
                if next_node not in visited:
                    heapq.heappush(queue, (cost + weight, next_node, path + [next_node]))

    return float("inf"), []

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

start = 'A'
goal = 'F'

cost, path = uniform_cost_search(graph, start, goal)

print("Minimum Cost:", cost)
print("Path:", " -> ".join(path))