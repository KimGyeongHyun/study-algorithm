# -*- coding: utf-8 -*-
# 벨만 포드 알고리즘
# 최단경로 알고리즘
# 음수 간선, 음수 순환의 경우에도 사용할 수 있음
# 다만 다익스트라와 비교하여 더 느림

# 벨만 포드의 경우 모든 간선을 확인하지만
# 다익스트라는 인접한 간선만 확인한다 (매번 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택)

import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    dist[start] = 0

    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost

                # n 번의 순환에서도 값이 갱신되었다면 음수 순환이 존재
                if i == n-1:
                    return True
                
    return False

n, m = map(int, input().split())
edges = []
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

negative_cycle = bf(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])