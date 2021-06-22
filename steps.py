steps = [1,2]

def find_all_possibilities(n):
    if n == 1 or n == 2 or n == 0:
        return n
        
    return find_all_possibilities(n-1) + find_all_possibilities(n-2)

print(find_all_possibilities(25))

