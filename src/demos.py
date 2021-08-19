print("Algotithms file loaded")


def quick_sort(arr):
    """
    Input: Unsorted List of Integers
    Returns: Sorted list of integers using QuickSort
    Note: This is ot an in-place implementation
    """

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1] 
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)

        return quick_sort(smaller) + equal + quick_sort(larger)

def merge_sorted(arr1, arr2):
    i, j = 0, 0
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
        
    return result_arr


def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = merge_sort(arr[:middle])
        l2 = merge_sort(arr[middle:])

        return merge_sorted(l1, l2)


def bubble_sort(arr):
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
    
    return arr