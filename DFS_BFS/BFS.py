# -*- coding: utf-8 -*-
from collections import deque

# DFS �� ����Լ��� ����ߴٸ� BFS �� ť �ڷᱸ���� ���
def bfs(graph, start, visited):

    # ť �ڷ����, ���� ���� �ʱ�ȭ
    queue = deque([start])
    visited[start] = True   # �湮 ���� ����

    while queue:    # ť �ȿ� �ڷᰡ ���� ������ �ݺ�
        v = queue.popleft() # ť pop
        print(v, end=' ')   # �ش� ��� ��ȸ

        for i in graph[v]:      # �ش� ����� ���� ��� ��ȸ
            if not visited[i]:  # �湮���� �ʾҴٸ�
                queue.append(i) # ť�� �߰�
                visited[i] = True   # �湮 ���� ����


# �� ��尡 ����� ������ ǥ��
graph = [
    [],         # 0�� �ε����� ����
    [2, 3, 8],  # 1�� ���� ����� ���
    [1, 7],     # 2�� ~
    [1, 4, 5],  # 3�� ~
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)