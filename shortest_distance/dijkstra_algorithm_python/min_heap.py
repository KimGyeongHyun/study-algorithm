# -*- coding: utf-8 -*-
# 힙 구현
# 데이터의 대략적인 순서를 가지는 완전 이진 트리 형태의 자료구조
# 완전 이진 트리이지만 배열로 쉽게 구현 가능
# 인덱스 0은 None 으로 비우고 1부터 노드를 채워 나간다면
# 해당 노드가 몇 번째 깊이에 있는지 쉽게 찾을 수 있음 (2^n)
# 즉 부모 노드를 쉽게 찾을 수 있음
# [None, 1, 4, 2, ...]
# min heap 은 루트 노드가 최저값을 가지고 자식 노드가 큰 값을 가짐


class Heap:
    def __init__(self):
        self.heap = []
        self.heap.append(None)


    # 해당 노드가 부모의 노드보다 작은지 비교
    # 힙 구조에 데이터 삽입할 때 사용
    def check_swap_up(self, idx):

        # 삽입한 모드의 부모 노드가 없을 경우 (루트 노드인 경우)
        if idx <= 1:
            return False

        parent_idx = idx // 2   # 부모 노드 인덱스

        if self.heap[idx] < self.heap[parent_idx]:
            return True
        else:
            return False

    # 데이터 삽입
    # 1) 마지막 노드에 새로운 노드 추가
    # 2) 추가된 새로운 노드를 부모의 노드와 비교하여 교환
    # 3) 부모 노드와 교환할 필요가 없을 때까지 1, 2번 반복
    def insert(self, data):

        self.heap.append(data)
        idx = len(self.heap) - 1    # 1)

        while self.check_swap_up(idx):  # 3)

            # 2)
            parent_idx = idx // 2

            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx

        return True

    # 해당 노드가 자식 노드보다 작은지 비교
    # 데이터 삭제에 사용
    def check_swap_down(self, idx):
        
        left_idx = idx * 2
        right_idx = idx * 2 + 1

        # 자식 노드가 하나도 없을 경우
        if left_idx >= len(self.heap):
            return False

        # 왼쪽 자식 노드만 있을 경우
        elif right_idx >= len(self.heap):
            if self.heap[left_idx] < self.heap[idx]:
                self.flag = 1
                return True
            else:
                return False

        # 자식 노드가 모두 있을 경우
        else:
            # 자식 노드 대소 비교 후 그 중 작은 노드와 바꿀지 결정
            if self.heap[left_idx] < self.heap[right_idx]:
                if self.heap[left_idx] < self.heap[idx]:
                    self.flag = 1
                    return True
                else:
                    return False
            else:
                if self.heap[right_idx] < self.heap[idx]:
                    self.flag = 2
                    return True
                else:
                    return False

    # 데이터 삭제 (삭제와 출력 동시에 수행)
    # 1) 루트 노드 리턴
    # 2) 힙의 마지막 노드를 루트 노드 자리에 놓음
    # 3) 루트 노드에서 자식 노드들과 크기를 비교해 바꿀지 결정하고 바꿈
    # 4) 3의 과정을 끝까지 수행
    def pop(self):

        # 힙에 데이터가 없다면
        if len(self.heap) <= 1:
            return None

        # 1), 2)
        max = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        idx = 1

        # 0 : False, 1 : 왼쪽 자식과 swap, 2 : 오른쪽 자식과 swap
        self.flag = 0

        while self.check_swap_down(idx):    # 4)
            left_idx = idx * 2
            right_idx = idx * 2 + 1

            # 3)
            if self.flag == 1:
                self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
                idx = left_idx
            elif self.flag == 2:
                self.heap[idx], self.heap[right_idx] = self.heap[right_idx], self.heap[idx]
                idx = right_idx
        
        return max


if __name__ == "__main__":
    my_heap = Heap()
    my_heap.insert(3)
    my_heap.insert(5)
    my_heap.insert(2)
    my_heap.insert(4)
    my_heap.insert(1)

    print(my_heap.pop())
    print(my_heap.pop())
    print(my_heap.pop())
    print(my_heap.pop())
    print(my_heap.pop())
    print(my_heap.pop())