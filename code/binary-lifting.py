
# binary lifting technique

arr = [1, 3, 8, 2, 9, 2, 5, 6]
arr.sort()

print(arr)

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

print(binary_search(arr, 5))