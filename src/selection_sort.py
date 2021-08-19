def selection_sort(arr):
    spot_marker = 0
    comparisions = 0
    while spot_marker < len(arr):
        comparisions += 1
        for num in range(spot_marker, len(arr)):
            comparisions += 1
            if arr[num] < arr[spot_marker]:
                arr[spot_marker], arr[num] = arr[num], arr[spot_marker]
        spot_marker += 1
    print(f"Comparition: {comparisions}")
    print(arr)


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
# l = [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1]
# l = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]

selection_sort(l)
