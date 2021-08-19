def buble_sort(arr):
    swap_happendes = True
    comparisions = 0
    while swap_happendes:
        comparisions += 1
        print(f"bubble sort status: {arr}")
        swap_happendes = False
        for num in range(len(arr) - 1):
            comparisions += 1
            if arr[num] > arr[num + 1]:
                swap_happendes = True
                arr[num], arr[num+1] = arr[num+1], arr[num]
    print(f"Comparition: {comparisions}")
    print(arr)


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
# l = [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1]
# l = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]

buble_sort(l)
