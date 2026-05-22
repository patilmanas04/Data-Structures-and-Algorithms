from utils.stack import Stack


class Queue:
    def __init__(self, capacity) -> None:
        self.stack = Stack(capacity)
        self.tempStack = Stack(capacity)
        self.capacity = capacity

    def enqueue(self, value):
        self.stack.push(value)

    def dequeue(self):
        if self.tempStack.isEmpty():
            while not self.stack.isEmpty():
                self.tempStack.push(self.stack.pop())
        return self.tempStack.pop()

    def __str__(self) -> str:
        return str(self.stack)


queue = Queue(5)

for i in range(5):
    queue.enqueue(i + 1)

print(queue)

# print(queue.enqueue(6)) # This will throw an error

print(queue.dequeue())
print(queue)

print(queue.dequeue())
print(queue)

print(queue.dequeue())
print(queue)

queue.enqueue(6)
print(queue)

queue.enqueue(7)
print(queue)

print(queue.dequeue())
print(queue)

print(queue.dequeue())
print(queue)

print(queue.dequeue())
print(queue)

print(queue.dequeue())
print(queue)

# print(queue.dequeue()) # This will throw an error
# print(queue)
