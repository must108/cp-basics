import heapq

arr = [1, 6, 3, 15, 64, 6, -1]

heapq.heapify(arr)

print(arr)

heapq.heappop(arr)
print(arr)