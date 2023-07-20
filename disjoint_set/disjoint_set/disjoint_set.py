class UnionFind:
    """최적화 이전의 union find"""

    def __init__(self, n) -> None:
        self.l = [i for i in range(n)]
    
    def find(self, u) -> int:
        """u 노드의 루트 노드 리턴"""
        par = self.l[u]
        if par == u:
            return u
        return self.find(self.l[u])

    def union(self, u, v) -> None:
        """v 노드의 부모 노드를 u 노드의 루트노드로 바꿈"""
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return
        
        if u != v:
            self.l[v] = u
    

class UnionFindOp:
    """union find 코드 최적화"""

    def __init__(self, n) -> None:
        self.l = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def find(self, u) -> int:
        """u 노드의 루트 노드 리턴"""
        par = self.l[u]
        if par == u:
            return u
        # 노드의 부모노드를 루트 노드로 바꾼다
        self.l[u] = self.find(self.l[u])
        return self.l[u]

    def union(self, u, v) -> None:
        """v 노드의 부모 노드를 u 노드의 루트노드로 바꿈"""
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return

        # a: 깊이가 더 깊은 노드
        if self.rank[u] < self.rank[v]:
            a, b = v, u
        else:
            a, b = u, v

        if self.rank[u] == self.rank[v]:
            self.rank[b] += 1

        self.l[a] = b
