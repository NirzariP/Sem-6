def ford_fulkerson(G, source, sink):
    max_flw = 0
    allpath,path_flws = [],[]
    while True:
        paths = bfs(G, source, sink)
        if not paths:
            break
        for path in paths:
            path_flw = min(G[path[i]][path[i+1]] for i in range(len(path)-1))
            allpath.append(path)
            path_flws.append(path_flw)
            max_flw += path_flw
            G = modify_G(G, path, path_flw)
    return max_flw, allpath, path_flws

def bfs(G, source, sink):
    paths = []
    queue = [(source, [source])]
    front = 0
    while front < len(queue):
        u, path = queue[front]
        front += 1
        for v, capacity in enumerate(G[u]):
            if capacity > 0 and v not in path:
                if v == sink:
                    paths.append(path + [v])
                else:
                    queue.append((v, path + [v]))
    return paths

def modify_G(G, path, flw):
    for i in range(len(path)-1):
        u, v = path[i], path[i+1]
        G[u][v] -= flw
        G[v][u] += flw  
    return G

# Graph representation
G = [[0, 9, 8, 0, 0, 0],
     [0, 0, 0, 4, 4, 0],
     [0, 2, 0, 0, 5, 3],
     [0, 0, 0, 0, 0, 5],
     [0, 0, 0, 0, 0, 6],
     [0, 0, 0, 0, 0, 0]]

source = 0
sink = 5
max_flw, allpath, path_flws = ford_fulkerson(G, source, sink)
print(f"Maximum flow: {max_flw}")
print("<-----All augmenting paths and their corresponding flows----->")
for i, path in enumerate(allpath):
    print(f"Path --> {path}, flow along path: {path_flws[i]}")
