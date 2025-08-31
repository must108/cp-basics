
arr = [1, 3, 8, 2, 9, 2, 5, 6]
arr.sort()

print(arr)

def binsearch(arr, val):
    a, b = 0, len(arr) - 1
    while a <= b:
        m = a + (b-a) // 2
        if arr[m] == val:
            return val, m
        elif arr[m] > val:
            b = m - 1
        else:
            a = m + 1    

print(binsearch(arr, 5))