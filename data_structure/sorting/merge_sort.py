def merge(left, right):
    i,j = 0,0
    arr= []
    while((i<len(left)) and (j<len(right))):
        if left[i] < right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1

    if i==len(left):
        arr.extend(right[j:])

    if j==len(right):
        arr.extend(left[i:])

    return arr

def mergeSort(list):
    if len(list) < 2:
        return list

    mid = int(len(list)/2)

    left = mergeSort(list[:mid])
    right = mergeSort(list[mid:])

    return merge(left, right)


unsorted = [1,5,2,3,7,4,9]

print(mergeSort(unsorted))
