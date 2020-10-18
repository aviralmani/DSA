def heapify(arr, n, parent):
    left_child = parent*2 + 1
    right_child = parent*2 + 2
    largest = parent

    if left_child < n and arr[left_child] > arr[parent]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[parent]:
        largest = right_child

    if parent < largest:
        arr[parent], arr[largest] = arr[largest], arr[parent]
        heapify(arr, n, largest)
    print('*****>>>>', arr)

def heap_sort(arr):
    n = len(arr)
    sorted = []
    for parent in range(int(n//2)-1, -1, -1):   #since n/2 -1 is the last parent
        heapify(arr, n, parent)

    print(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

arr = [4,1,7,2,5,3]

sorted_arr = heap_sort(arr)
print(sorted_arr)
