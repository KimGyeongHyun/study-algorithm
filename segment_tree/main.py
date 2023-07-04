
l = [1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5]
tree = [0 for _ in range(len(l) * 4)]

def init(start=0, end=len(l)-1, input_node=1):
    if start == end:
        tree[input_node] = l[start]
        return tree[input_node]
    mid = (start + end) // 2
    tree[input_node] = init(start, mid, input_node * 2) + init(mid+1, end, input_node*2+1)
    return tree[input_node]

def sum(left, right, start=0, end=len(l)-1, input_node=1):
    """left ~ right index 의 총합 반환"""
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[input_node]
    mid = (start + end) // 2
    return sum(left, right, start, mid, input_node*2) + sum(left, right, mid+1, end, input_node*2+1)

def update(index, dif, start=0, end=len(l)-1, input_node=1):
    if index < start and index > end:
        return
    tree[input_node] += dif
    if start == end:
        return
    mid = (start + end) // 2
    update(index, dif, start, mid, input_node*2)
    update(index, dif, mid+1, end, input_node*2+1)

init()
# print(*tree)
print(sum(0, 0))
print(sum(0, 1))
print(sum(0, 2))
print(sum(0, 3))
print(sum(0, 4))
print(sum(1, 1))
print(sum(1, 2))
print(sum(1, 3))
print(sum(1, 4))

