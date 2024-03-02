from task_1 import metro_network

def dfs_paths(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        yield path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            yield from dfs_paths(graph, neighbor, end, path + [neighbor])

def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in graph.neighbors(vertex):
            if neighbor not in path:
                if neighbor == end:
                    yield path + [neighbor]
                else:
                    queue.append((neighbor, path + [neighbor]))

if __name__ == "__main__":
    start_station = "Tsentralniy Rinok"
    end_station = "Naukova"

    dfs_result = list(dfs_paths(metro_network, start_station, end_station))
    bfs_result = list(bfs_paths(metro_network, start_station, end_station))

    print("\n")
    print("DFS Paths:")
    for path in dfs_result:
        print(' => '.join(path))

    print("\nBFS Paths:")
    for path in bfs_result:
        print(' => '.join(path))
    print("\n")
