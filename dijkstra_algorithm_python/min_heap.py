# -*- coding: utf-8 -*-
# �� ����
# �������� �뷫���� ������ ������ ���� ���� Ʈ�� ������ �ڷᱸ��
# ���� ���� Ʈ�������� �迭�� ���� ���� ����
# �ε��� 0�� None ���� ���� 1���� ��带 ä�� �����ٸ�
# �ش� ��尡 �� ��° ���̿� �ִ��� ���� ã�� �� ���� (2^n)
# �� �θ� ��带 ���� ã�� �� ����
# [None, 1, 4, 2, ...]
# min heap �� ��Ʈ ��尡 �������� ������ �ڽ� ��尡 ū ���� ����


class Heap:
    def __init__(self):
        self.heap = []
        self.heap.append(None)


    # �ش� ��尡 �θ��� ��庸�� ������ ��
    # �� ������ ������ ������ �� ���
    def check_swap_up(self, idx):

        # ������ ����� �θ� ��尡 ���� ��� (��Ʈ ����� ���)
        if idx <= 1:
            return False

        parent_idx = idx // 2   # �θ� ��� �ε���

        if self.heap[idx] < self.heap[parent_idx]:
            return True
        else:
            return False

    # ������ ����
    # 1) ������ ��忡 ���ο� ��� �߰�
    # 2) �߰��� ���ο� ��带 �θ��� ���� ���Ͽ� ��ȯ
    # 3) �θ� ���� ��ȯ�� �ʿ䰡 ���� ������ 1, 2�� �ݺ�
    def insert(self, data):

        self.heap.append(data)
        idx = len(self.heap) - 1    # 1)

        while self.check_swap_up(idx):  # 3)

            # 2)
            parent_idx = idx // 2

            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx

        return True

    # �ش� ��尡 �ڽ� ��庸�� ������ ��
    # ������ ������ ���
    def check_swap_down(self, idx):
        
        left_idx = idx * 2
        right_idx = idx * 2 + 1

        # �ڽ� ��尡 �ϳ��� ���� ���
        if left_idx >= len(self.heap):
            return False

        # ���� �ڽ� ��常 ���� ���
        elif right_idx >= len(self.heap):
            if self.heap[left_idx] < self.heap[idx]:
                self.flag = 1
                return True
            else:
                return False

        # �ڽ� ��尡 ��� ���� ���
        else:
            # �ڽ� ��� ��� �� �� �� �� ���� ���� �ٲ��� ����
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

    # ������ ���� (������ ��� ���ÿ� ����)
    # 1) ��Ʈ ��� ����
    # 2) ���� ������ ��带 ��Ʈ ��� �ڸ��� ����
    # 3) ��Ʈ ��忡�� �ڽ� ����� ũ�⸦ ���� �ٲ��� �����ϰ� �ٲ�
    # 4) 3�� ������ ������ ����
    def pop(self):

        # ���� �����Ͱ� ���ٸ�
        if len(self.heap) <= 1:
            return None

        # 1), 2)
        max = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        idx = 1

        # 0 : False, 1 : ���� �ڽİ� swap, 2 : ������ �ڽİ� swap
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