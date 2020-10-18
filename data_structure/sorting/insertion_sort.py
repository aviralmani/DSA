def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j= i-1
        while j>=0 and key< arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

    return arr

unsorted = [3,5,1,7,6,2,4]
print('unsorted:', unsorted)
sorted = insertion_sort(unsorted)

print('sorted:', sorted)
