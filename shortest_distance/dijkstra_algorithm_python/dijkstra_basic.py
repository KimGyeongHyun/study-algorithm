# -*- coding: utf-8 -*-

# 다익스트라 알고리즘은 방향(무방향) 그래프에서 
# 어느 한 노드를 기준으로 다른 노드로 가는 최단거리를 구하는 알고리즘이다
# 해당 알고리즘은 한 노드를 기준으로만 최단거리를 구할 수 있기 때문에
# 모든 노드를 기준으로 다른 노드로 가는 최단거리를 구하기 위해선 
# 플로이드 워셜 알고리즘이 필요하다

# 플로이드 워셜 알고리즘의 시간 복잡도는 O(n*3),
# 다익스트라 알고리즘은 O(nlog(n)) 이다
# 따라서 노드 수가 적고 모든 최단거리를 확인하기 위해선 플로이드,
# 하나의 최단거리만 알면 되거나 간선이 많으면 다익스트라 알고리즘을 활용하면 된다

# -구성
# 방향 그래프, 최단거리를 저장할 리스트, 방문 여부 리스트
# 방향 그래프 -> graph[출발 노드][(도착 노드, 거리), (도착 노드, 거리) ...]

# -작동 방식
# 노드별 최단거리를 구할 노드를 선택 -> 시작 노드라고 별칭
# 시작 노드의 최단거리를 0, 방문 여부를 True 설정
# 시작 노드 주변 노드 거리를 그래프를 통해 최단거리 리스트에 갱신
# (===== 부분은 모든 노드를 방문할 때까지 반복)
# =====================================================
# 방문하지 않은 노드 중 최단거리가 가장 짧은 노드 선택 -> 중간 노드라고 별칭
# 중간 노드에서 도착할 수 있는 노드 모두 탐색   (----- 부분 반복)
# ------------------------------------------------------
# 도착 노드 기준 "시작 노드 -> 중간 노드" + "중간 노드 -> 도착 노드" < "현재 최단거리" 라면
# 해당 값으로 최단거리를 갱신함
# ------------------------------------------------------
# ======================================================


import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())
# key : 출발 노드, value : (도착 노드, 거리)
graph = [[] for i in range(n+1)]
# 방문 여부 리스트
# key : 노드, value : 방문 여부
visited = [False] * (n + 1)
# 최단 거리 저장할 리스트
# key : 노드, value : 최단 길이
distance = [INF] * (n + 1)

# 간선 입력
for _ in range(m):
    # 출발 노드, 도착 노드, 거리
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중 최단 거리 짧은 노드 반환
def get_smallest_node():
    min_value = INF     # 최단 거리
    index = 0           # 최단 거리 노드 인덱스
    for i in range(n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True

    # 시작 노드에서 주변 노드 거리 탐색 후 distance 리스트에 갱신
    for i in graph[start]:
        # i[0] : 도착 노드, i[1] : 거리
        distance[i[0]] = i[1]

    for i in range(n-1):

        # 중간 노드 (최단 거리 순으로 결정)
        now = get_smallest_node()
        # 중간 노드 방문 여부 갱신
        visited[now] = True

        # 중간 노드에서 도착할 수 있는 노드 순환
        for j in graph[now]:
            # now : 중간 노드
            # distance[now] : 현 시점 시작 노드 -> 중간 노드 최단 거리
            # j[1] : 중간 노드 -> 도착 노드 거리
            cost = distance[now] + j[1]
            # j[0] : 도착 노드, distance[j[0]] : 현 시점 시작 노드 -> 도착 노드 최단 거리
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):

    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


# input
# 6 11
# 1    
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

# output
# 0
# 2
# 3
# 1
# 2
# 4