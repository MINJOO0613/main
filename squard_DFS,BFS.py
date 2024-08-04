# 08.01 우재튜터님 DFS BFS 코드 구현

# 양방향 그래프(무방향 그래프)
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
# DFS_iterative(while 반복문)
def iterative_dfs(graph, start_v):
    visited = []
    stack = [start_v]
    while stack:
        curr_v = stack.pop()
        if curr_v not in visited:
            visited.append(curr_v)
            for v in graph[curr_v]:
                stack.append(v)

    return visited

rlt = iterative_dfs(graph, "A")
print(rlt)      #['A', 'C', 'F', 'E', 'B', 'D']

# DFS_recursive(재귀함수)
def recursive_dfs(graph, visited, start_v):
    curr_v = start_v
    if curr_v not in visited:
        visited.append(curr_v)

        for v in graph[curr_v]:
            recursive_dfs(graph, visited, v)

visited = []
recursive_dfs(graph, visited, "A")
print(visited)      #['A', 'B', 'D', 'E', 'F', 'C']


# BFS_Queue
from collections import deque

def bfs(graph, start_v):
    visited = []
    # queue = [start_v]
    queue = deque([start_v])

    while queue:
        # curr_v = queue.pop(0)  # O(n)
        curr_v = queue.popleft()
        if curr_v not in visited:
            visited.append(curr_v)
            for v in graph[curr_v]:
                queue.append(v)

    return visited

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

result = bfs(graph, "A")
print(result)

