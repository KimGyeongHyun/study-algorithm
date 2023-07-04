class SegmentTree:

    def __init__(self, input_l) -> None:
        self.l = input_l
        self.tree = [0 for _ in range(len(self.l)*4)]
        self._set_tree(0, len(self.l)-1, 1)
        
    def _set_tree(self, start, end, tree_idx):
        if start == end:
            self.tree[tree_idx] = self.l[start]
            return self.tree[tree_idx]
        mid = (start + end) // 2
        left = self._set_tree(start, mid, tree_idx*2)
        right = self._set_tree(mid+1, end, tree_idx*2+1)
        self.tree[tree_idx] = left + right
        return self.tree[tree_idx]

    def get_sum(self, left, right, start, end, tree_idx):
        if left > end or right < start:
            return 0
        
        # 부등호가 들어가는 이유는 공백인 노드도 있기 때문
        # 데이터 범위가 늘어나면서 값을 찾기 때문에
        # 찾는 범위가 나올 때 리턴하게 되면
        # 불필요한 데이터 범위가 들어가지 않음
        if left <= start and end <= right:
            return self.tree[tree_idx]
        
        mid = (start + end) // 2
        v_left = self.get_sum(left, right, start, mid, tree_idx*2)
        v_right = self.get_sum(left, right, mid+1, end, tree_idx*2+1)
        return v_left + v_right
    
    def update(self, idx, dif, start, end, tree_idx):

        if idx < start or end < idx:
            return
        
        self.tree[tree_idx] += dif
        
        if start == end:
            return
        
        mid = (start + end) // 2
        self.update(idx, dif, start, mid, tree_idx*2)
        self.update(idx, dif, mid+1, end, tree_idx*2+1)


if __name__ == "__main__":
    l = [1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5]
    seg = SegmentTree(l)
    print(seg.get_sum(4, 8, 0, len(l)-1, 1))
    seg.update(5, -5, 0, len(l)-1, 1)
    print(seg.get_sum(4, 8, 0, len(l)-1, 1))
    
