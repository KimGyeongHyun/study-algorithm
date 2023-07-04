import random


# [1, 2, 3, 4, 5]

class Sort :
    def bubble_sort(arr):
        """바로 옆에 있는 요소와 비교, 정렬"""

        # 12, 23, 34, 45, 23, 34, 45, 34, 45, 45

        for i in range(len(arr)):   # 처음부터 시작
            for j in range(len(arr) - i - 1):
                print(i, j)
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


    def selection_sort(arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left, right, equal = [], [], []
        for i in arr:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                equal.append(i)
        return quick_sort(left) + equal + quick_sort(right)


    def merge_sort(arr):
        if len(arr) < 2:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        merged_arr = []
        l = r = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                merged_arr.append(left[l])
                l += 1
            else:
                merged_arr.append(right[r])
                r += 1

        merged_arr += left[l:]
        merged_arr += right[r:]
        return merged_arr


    def heap_sort(arr):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[i] < arr[l]:
                largest = l

            if r < n and arr[largest] < arr[r]:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(arr)
        for i in range(n, -1, -1):
            heapify(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

        return arr



    def radix_sort(arr):
        RADIX = 10
        placement = 1

        max_digit = max(arr)

        while placement < max_digit:
            buckets = [list() for _ in range(RADIX)]

            for i in arr:
                tmp = int((i / placement) % RADIX)
                buckets[tmp].append(i)

            a = 0
            for b in range(RADIX):
                buck = buckets[b]
                for i in buck:
                    arr[a] = i
                    a += 1

            placement *= RADIX

        return arr


    def counting_sort(arr):
        max_value = max(arr)
        m = max_value + 1
        count = [0] * m

        for a in arr:
            count[a] += 1

        i = 0
        for a in range(m):
            for c in range(count[a]):
                arr[i] = a
                i += 1
        return arr


arr = [i for i in random.sample(range(10), 10)]


print("Original array: ", arr)
print("Bubble sort: ", Sort.bubble_sort(arr))
print("Selection sort: ", Sort.selection_sort(arr))
print("Quick sort: ", Sort.quick_sort(arr))
print("Merge sort: ", Sort.merge_sort(arr))
print("Heap sort: ", Sort.heap_sort(arr))
print("Radix sort: ", Sort.radix_sort(arr))
print("Counting sort: ", Sort.counting_sort(arr))