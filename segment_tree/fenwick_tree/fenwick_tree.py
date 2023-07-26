import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def LSBIT(n):
    return n & -n


def prefix_sum(idx):
    sum = 0
    while idx > 0:
        sum += tree[idx]
        idx -= LSBIT(idx)

    return sum


def get_sum(a, b):
    return prefix_sum(b) - prefix_sum(a-1)


def update_tree(idx, dif):

    while idx <= len(l) - 1:
        tree[idx] += dif
        idx += LSBIT(idx)


def set_tree():
    for i in range(1, len(tree)):
        update_tree(i, l[i])


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    l = [0]
    tree = [0 for _ in range(n+1)]
    for _ in range(n):
        l.append(int(input()))
    set_tree()

    for _ in range(m+k):
        t = list(map(int, input().split()))
        if t[0] == 1:
            dif = t[2] - l[t[1]]
            update_tree(t[1], dif)
            l[t[1]] = t[2]
        elif t[0] == 2:
            print(get_sum(t[1], t[2]))