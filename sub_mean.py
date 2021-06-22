def sub_to_mean(curr, n, x):
    return ((curr*n)-x)/(n-1)

def sub_mean(arr : list, v : float):
    start = 0
    end = len(arr) - 1
    current_mean = mean(arr)
    nelems = len(arr)

    while end >= start:
        if current_mean == v:
            print(arr[start:end])
            return True
        
        elif start == end and arr[start] != v:
            return False
    
        if current_mean > v:
            current_mean = sub_to_mean(current_mean, nelems, arr[end])
            end -= 1
        else:
            current_mean = sub_to_mean(current_mean, nelems, arr[start])
            start += 1
        
        nelems -= 1

    return False


def mean(arr):
    return sum(arr)/len(arr)

arr = [1,3,5,7,8,9,15,16,17]
print(sub_mean(
    arr,
    12
))