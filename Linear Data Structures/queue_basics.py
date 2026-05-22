from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print(queue)

for i in range(3):
    print(queue.popleft())
    print(queue)

queue.append(6)
queue.append(7)
print(queue)

print(queue.popleft())
print(queue)

print(queue.popleft())
print(queue)
