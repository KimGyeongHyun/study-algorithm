# -*- coding: utf-8 -*-


def dfs(graph, v, visited):
    
    # v 노드 방문
    # 방문하지 않은 인접 노드가 없을 때까지 파고 들어감
    
    visited[v] = True   # 방문 여부 설정
    print(v, end=" ")   # 해당 노드 순회

    for i in graph[v]:      # 해당 노드와 인접한 노드 순회
        if not visited[i]:  # 방문하지 않았다면
            dfs(graph, i, visited)  # 인접한 노드 재귀

# 각 노드가 연결된 정보를 표현
graph = [
    [],         # 0번 인덱스는 무시
    [2, 3, 8],  # 1번 노드와 연결된 노드
    [1, 7],     # 2번 ~
    [1, 4, 5],  # 3번 ~
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)