from collections import deque

queue = deque()
stack = []

for i in range(5):
    queue.append(i + 1)

print(queue)

# Reversing the queue using stack
for i in range(5):
    stack.append(queue.popleft())

print(f"stack({stack})")
print(queue)

for i in range(5):
    queue.append(stack.pop())

print(f"stack({stack})")
print(queue)
