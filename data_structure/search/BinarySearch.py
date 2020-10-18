def binary_Search(arr, x):
    l = len(arr)
    last = l -1
    initial = 0

    while (initial<=last):              #IMP
        mid = int((initial+last)/2)

        if arr[mid] == x:
            return mid+1                # +1 because we want to return actual index (i.e from 1 to N)

        elif arr[mid] < x:
            initial = mid + 1           #IMP

        elif arr[mid] > x:
            last = mid -1               #IMP

    return -1

arr = [1,2,3,4,5,6,7,8]

print(binary_Search(arr, 7))
