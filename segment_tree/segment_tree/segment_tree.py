class SegmentTree:

    def __init__(self, input_l) -> None:
        self.l = input_l
        self.tree = [0 for _ in range(len(self.l)*4)]
        self._set_tree(0, len(self.l)-1, 1)
        
    def _set_tree(self, start, end, tree_idx):
        """
        재귀적으로 돌면서 세그먼트 트리 구성 \n
        1 은 루트 노드, 수의 모든 합 저장 \n
        리프 노드는 l 의 수 저장 \n
        start, end 규칙에 따라 노드 갱신 \n
        수 배열 l의 start에서 end까지의 수의 총합을 세그먼트 트리의 tree_idx 에 저장 \n
        
        start: 수 배열 l 의 시작 인덱스 \n
        end: 수 배열 l 의 마지막 인덱스 \n
        tree_idx: 합친 수를 적용할 트리의 인덱스 \n
        """
        
        # 자식 노드로 내려가다가 인덱스가 같아진다면 
        if start == end:
            self.tree[tree_idx] = self.l[start]     # 트리에 l[start] 갱신
            return self.tree[tree_idx]              # 해당 값 리턴
        
        # start, end 를 반씩 나눠 재귀 수행
        # 이진 트리는 루트 노드가 1이라면 *2를 통해 자식 노드에 쉽게 다가갈 수 있는 특징을 사용
        mid = (start + end) // 2
        left = self._set_tree(start, mid, tree_idx*2)       # 자식 노드 우선 갱신
        right = self._set_tree(mid+1, end, tree_idx*2+1)    # 자식 노드 우선 갱신
        self.tree[tree_idx] = left + right                  # 양쪽의 총합을 본인 노드에 갱신
        return self.tree[tree_idx]                          # 본인 리턴

    def get_sum(self, left, right, start, end, tree_idx):
        """left ~ right 까지의 총합 리턴"""

        # 값이 꼬였다면 총합 0
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
        """
        l[idx] 값을 dif 만큼 변경 \n
        세그먼트 트리의 노드값만 변경
        """

        # 해당 인덱스가 범위 안에 없으면 탈출
        if idx < start or end < idx:
            return
        
        # 트리 노드 갱신 (총합 갱신)
        self.tree[tree_idx] += dif
        
        # 말단 노드라면 종료
        if start == end:
            return
        
        # 재귀적으로 갱신
        mid = (start + end) // 2
        self.update(idx, dif, start, mid, tree_idx*2)
        self.update(idx, dif, mid+1, end, tree_idx*2+1)


if __name__ == "__main__":
    l = [1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5]
    seg = SegmentTree(l)
    print(seg.get_sum(4, 8, 0, len(l)-1, 1))
    seg.update(5, -5, 0, len(l)-1, 1)
    print(seg.get_sum(4, 8, 0, len(l)-1, 1))
    
