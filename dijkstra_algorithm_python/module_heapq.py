import heapq

if __name__ == "__main__":
    heap = []

    heapq.heappush(heap, 10)
    heapq.heappush(heap, 6)
    heapq.heappush(heap, 13)
    heapq.heappush(heap, 5)

    print(heap)

    print(heapq.heappop(heap))
    print(heap)