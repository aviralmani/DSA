def binary_search(arr, val, start, end):
    if start == end:
        if val > arr[start]:
            return start + 1
        else:
            return start

    if start > end:
        return start

    mid = (start+end)/2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # j= i-1
        j = binary_search(arr, key, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]

    return arr


unsorted = [3,5,1,7,6,2,4]
print('unsorted:', unsorted)
sorted = insertion_sort(unsorted)

print('sorted:', sorted)
