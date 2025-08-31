
arr = [1, 3, 8, 2, 9, 2, 5, 6]

def bubble(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

print(bubble(arr))