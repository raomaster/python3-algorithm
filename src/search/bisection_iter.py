def bisection_iter(n, arr):
    start = 0
    stop = len(arr) - 1
    while start <= stop:
        mid = (start + stop)//2
        print(mid)
        if n == arr[mid]:
            return f"{n} found at index: {mid}"
        elif n > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1 
    print(f"start={start}")
    print(f"stop={stop}")
    return f"{n} not found in list"
        
def bisection_iter_v2(n, arr, start, stop):
    if start > stop:
        return f"{n} not found in list"
    else:
        mid = (start + stop)//2
        if n == arr[mid]:
            return f"{n} Found in index: {mid}"
        elif n > arr[mid]:
            return bisection_iter_v2(n, arr, mid + 1, stop)
        else:
            return bisection_iter_v2(n, arr, start, mid-1)
    


def create_list(max_val):
    arr = []
    for num in range(1, max_val):
        arr.append(num)
    return arr


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_to_search = 9

print(bisection_iter_v2(num_to_search, l,0 ,len(l)-1))