
# binary lifting technique

def binary_search(arr, x):
    n = len(arr)
    k = 0
    b = n // 2

    while b >= 1:
        while k + b < n and arr[k+b] <= x:
            k += b
        b //= 2
    if arr[k] == x:
        return k
    return -1