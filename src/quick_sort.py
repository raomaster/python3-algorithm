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



l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

print(quick_sort(l))
