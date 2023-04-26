import heapq
import math

def cheapest_plan(fc, sc, tg, n, fuel_price, adj):
    
    edic = []
    h = []
    for i in range(n):
        for j in range(0, fc+1):
            edic.append((i,j))

    adj_dict = {u: {} for u in edic}
    for u, v in edic:
        if v < fc:
            adj_dict[(u,v)][(u,v+1)]= fuel_price[u]
        for i in range(n):
            if v >= fc*(3/4) and adj[u][i] != 0 and v - adj[u][i] > 0:
                adj_dict[(u,v)][(i,v-adj[u][i])] = 0   
    
    dist = dijkstra(adj_dict, (sc, 0))
    for i in range(fc+1):
        h.append(dist[(tg, i)])
        
    r = min(h)
    return r
    
    
def dijkstra(graph, source):
    dist = {v: math.inf for v in graph}
    dist[source] = 0

    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue

        for v, w in graph[u].items():
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist
