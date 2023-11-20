def selection_sort(arr):
    size = len(arr)
    for i in range(size -1):
        min_position = i
        for j in range(min_position+1 , size):
            if arr[j] < arr[min_position]:
                min_position = j
        arr[i], arr[min_position] = arr[min_position],arr[i]


if __name__ == '__main__':
    test =[
            [ 78, 12, 15, 8, 61, 27, 53, 23],
            [],
            [1,2,3,4],
            [5],
            [32,11,44,14,52,90,19],
            [0]
    ]
    for elements in test:
        selection_sort(elements)
        print(elements)



