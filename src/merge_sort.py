def merge_sorted(arr1, arr2):
    i, j = 0, 0
    print(f"Merge Left List: {arr1} \nMerge Right List: {arr2}")
    result_arr = []
    while i < (len(arr1)) and j < (len(arr2)):
        if arr1[i] <= arr2[j]:
            result_arr.append(arr1[i])
            i += 1
        else:
            result_arr.append(arr2[j])
            j += 1

    while j < len(arr2):
        result_arr.append(arr2[j])
        j += 1
    
    while i < len(arr1):
        result_arr.append(arr1[i])
        i += 1
        
    print(f"Sort Array: {result_arr}")
    return result_arr


def divide_arr(arr):
    if len(arr) < 2:
        print(f"Base condition reached with {arr[:]}")
        return arr[:]
    else:
        middle = len(arr)//2
        print(f"Current list: {arr}")
        print(f"Left Split", arr[:middle])
        print(f"Right split", arr[middle:])
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])

        return merge_sorted(l1, l2)

# l1 = [1, 4, 6, 8, 10]
# l2 = [2, 3, 5, 7, 8, 9]


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

# l = [8,6,2,5]

divide_arr(l)
