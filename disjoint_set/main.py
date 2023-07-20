from disjoint_set import disjoint_set
import time

GAP = 5
NUM = 100000

if __name__ == "__main__":
    start = time.time()
    for _ in range(1):
        a = disjoint_set.UnionFind(NUM)

        for gap in range(GAP, NUM, GAP):
            for i in range(gap, NUM, gap):
                a.union(i-(gap//2), i)
            
        for i in range(10):
            for j in range(NUM):
                a.find(i)

    print(time.time() - start)

    start = time.time()
    for _ in range(1):
        a = disjoint_set.UnionFindOp(NUM)
        
        for gap in range(GAP, NUM, GAP):
            for i in range(gap, NUM, gap):
                a.union(i-(gap//2), i)

        for i in range(10):
            for j in range(NUM):
                a.find(i)

    print(time.time() - start)

# 4.171007394790649
# 2.292194128036499

