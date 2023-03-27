# -*- coding: utf-8 -*-
from collections import deque

# DFS 가 재귀함수를 사용했다면 BFS 는 큐 자료구조를 사용
def bfs(graph, start, visited):

    # 큐 자료규조, 시작 노드로 초기화
    queue = deque([start])
    visited[start] = True   # 방문 여부 갱신

    while queue:    # 큐 안에 자료가 없을 때까지 반복
        v = queue.popleft() # 큐 pop
        print(v, end=' ')   # 해당 노드 순회

        for i in graph[v]:      # 해당 노드의 인접 노드 순회
            if not visited[i]:  # 방문하지 않았다면
                queue.append(i) # 큐에 추가
                visited[i] = True   # 방문 여부 갱신


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

bfs(graph, 1, visited)