def binary_Search(arr, find_value, low, high):
    if low <= high:
        mid = int((low+high)/2)

        if arr[mid] == find_value:
           return mid+1
        if arr[mid] < find_value:
            return binary_Search(arr, find_value, mid+1, high)
        else:
            return binary_Search(arr, find_value, low, mid-1)
    else:
        return -1

arr = [1,2,3,4,5,6,7,8]

print(binary_Search(arr, 2, 0, len(arr)-1))
