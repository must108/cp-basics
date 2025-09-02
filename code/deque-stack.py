
# deque (double ended queue)
from collections import deque

q = deque([1, 2, 3])

q.appendleft(5)
q.append(6)

print(q)

q.popleft()
q.pop()

print(q)

# stack

from collections import deque

q = deque([1, 2, 3])

q.append(4)
q.append(5)

print(q)

q.pop()
q.pop()

print(q)