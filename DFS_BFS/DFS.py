# -*- coding: utf-8 -*-


def dfs(graph, v, visited):
    
    # v ��� �湮
    # �湮���� ���� ���� ��尡 ���� ������ �İ� ��
    
    visited[v] = True   # �湮 ���� ����
    print(v, end=" ")   # �ش� ��� ��ȸ

    for i in graph[v]:      # �ش� ���� ������ ��� ��ȸ
        if not visited[i]:  # �湮���� �ʾҴٸ�
            dfs(graph, i, visited)  # ������ ��� ���

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

dfs(graph, 1, visited)