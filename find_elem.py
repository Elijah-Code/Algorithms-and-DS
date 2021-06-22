def is_in(arr, val):
    ix = 0
    while ix <= len(arr):
        if arr[ix] == val: return arr[ix]
        ix += 1


def findOnce(arr : list, n : int):
     
    start = 0
    end = n-1
    while start <= end:
        
        if start == n-1: return arr[start]
        
        mid = (end + start) // 2

        if mid % 2 == 0 and arr[mid] == arr[mid+1]:
            start = mid + 1

        if mid % 2 == 0 and arr[mid] != arr[mid+1]:
            end = mid - 1

        if mid % 2 != 0:
            if arr[mid] == arr[mid+1]:
                end = mid - 1
            else:
                start = mid + 1

    return arr[start]


def binary_search(arr : list, n : int, val : int):
    start = 0
    end = n-1
    while start <= end:
        mid = (end + start) // 2 

        if val > arr[mid]:
            start = mid+1
        else:
            end = mid-1

    return start



# A Binary search based function to find
# the element that appears only once
 
 

arr = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,9]
print(findOnce(arr,len(arr)))
