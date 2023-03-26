INF = 1_000_000_000


def get_min_index_with_v(arr, v):
    min = INF
    index = -1
    for i in range(len(arr)):
        if v[i] == False and arr[i] < min:
            min = arr[i]
            index = i

    return index


def get_dijkstra(input_arr, n):

    v = [False for _ in range(len(input_arr))]

    arr = input_arr[n]
    v[n] = True

    for _ in range(len(input_arr) - 1):
        
        index = get_min_index_with_v(arr, v)
        v[index] = True

        # print(index)

        for j in range(len(input_arr)):
            # print(" >> ", end='')
            # print(f'{j} {arr[index]} {input_arr[index][j]} {arr[j]}')

            if v[j] == False:
                if arr[index] + input_arr[index][j] < arr[j]:
                    arr[j] = arr[index] + input_arr[index][j]

        # print("arr >> ", end='')
        # print(arr, end='\n\n')

    return arr


if __name__ == "__main__":
    
    arr = [[0, 2, 5, 1, INF, INF],
    [2, 0, 3, 2, INF, INF],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, INF],
    [INF, INF, 1, 1, 0, 2],
    [INF, INF, 5, INF, 2, 0]]

    print(get_dijkstra(arr, 0))
