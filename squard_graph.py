# 08.02 임우재튜터님 백준 1260 문제 풀이_그래프(dfs/bfs)
import sys
sys.stdin = open('index.txt', 'r')

# N, M, V = map(int,input().split())
# graph = {}
# for _ in range(N):
#     start_v, end_v = map(int,input().split())
#     if start_v not in graph:
#         graph[start_v] = []
#     if end_v not in graph:
#         graph[end_v] = []
#     graph[start_v].append(end_v)
#     graph[end_v].append(start_v)
# print(graph)
N, M, V = map(int, input().split())
graph = {}

# input_build_graph
for v in range(1, N+1):
    graph[v] = []
for _ in range(M):
    start_v, end_v = map(int, input().split())
    graph[start_v].append(end_v)
    graph[end_v].append(start_v)            #양방향그래프를 표현하기 위해 이 코드가 필요함

# dfs
def dfs(graph, visited, start_v):
    # visited = []
    # stack = [V]
    #
    # while stack:
    #     current = stack.pop()
    #     if current not in visited:
    #         visited.append(current)
    #         for neighbor in graph[current]:
    #             stack.append(neighbor)
    # return visited
    current = start_v
    if current not in visited:
        visited.append(current)

        for v in sorted(graph[current]):
            dfs(graph, visited, v)

    return visited

visited = []
dfs(graph, visited, V)
print(" ".join(map(str, visited)))

from collections import deque

# bfs
def bfs(graph, start_v):
    visited = []
    queue = deque([start_v])

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.append(current)
            for v in sorted(graph[current]):
                queue.append(v)

    return visited

visited = bfs(graph, V)
print(" ".join(map(str, visited)))