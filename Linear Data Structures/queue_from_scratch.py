class Queue:
    def __init__(self, capacity) -> None:
        self.queue = [0] * capacity
        self.front = self.rear = -1
        self.capacity = capacity
        self.count = 0

    def enqueue(self, value):
        if self.count == self.capacity:
            raise IndexError("queue has already reached its maximum capacity")
        self.rear += 1
        self.rear = self.rear % self.capacity
        self.queue[self.rear] = value
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise IndexError("cannot dequeue from an empty queue")
        self.front += 1
        self.front = self.front % self.capacity
        value = self.queue[self.front]
        self.queue[self.front] = 0
        self.count -= 1
        return value

    def __len__(self):
        return self.count

    def __str__(self) -> str:
        string = "<["
        index = (self.front + 1) % self.capacity
        for _ in range(self.count):
            string += str(self.queue[index])
            string += ", " if index != self.rear else ""
            index = (index + 1) % self.capacity
        string += f"], 'queue', size={self.capacity}>"
        return string


queue = Queue(6)

for i in range(6):
    queue.enqueue(i + 1)

print(queue)
print(f"Length: {len(queue)}")

print()
print(f"Removed: {queue.dequeue()}")
print(queue)
print(f"Length: {len(queue)}")

print()
print(f"Removed: {queue.dequeue()}")
print(queue)
print(f"Length: {len(queue)}")

print()
print(f"Removed: {queue.dequeue()}")
print(queue)
print(f"Length: {len(queue)}")

print()
queue.enqueue(7)
print(queue)
print(f"Length: {len(queue)}")

print()
queue.enqueue(8)
print(queue)
print(f"Length: {len(queue)}")

print()
queue.enqueue(9)
print(queue)
print(f"Length: {len(queue)}")

# print()
# queue.enqueue(9) # This will throw an error as the queue is already full
# print(queue)
# print(f"Length: {len(queue)}")

print()
print(f"Removed: {queue.dequeue()}")
print(queue)
print(f"Length: {len(queue)}")

print()
print(f"Removed: {queue.dequeue()}")
print(queue)
print(f"Length: {len(queue)}")

print()
print(f"Removed: {queue.dequeue()}")
print(queue)
print(f"Length: {len(queue)}")

print()
print(f"Removed: {queue.dequeue()}")
print(queue)
print(f"Length: {len(queue)}")

print()
print(f"Removed: {queue.dequeue()}")
print(queue)
print(f"Length: {len(queue)}")

print()
print(f"Removed: {queue.dequeue()}")
print(queue)
print(f"Length: {len(queue)}")

# print()
# print(f"Removed: {queue.dequeue()}") # This will throw an error as the queue is empty at this point
# print(queue)
# print(f"Length: {len(queue)}")

print()
queue.enqueue(99)
print(queue)
print(f"Length: {len(queue)}")

print()
queue.enqueue(100)
print(queue)
print(f"Length: {len(queue)}")

print()
queue.enqueue(101)
print(queue)
print(f"Length: {len(queue)}")

print()
print(f"Removed: {queue.dequeue()}")
print(queue)
print(f"Length: {len(queue)}")

print()
print(f"Removed: {queue.dequeue()}")
print(queue)
print(f"Length: {len(queue)}")

print()
print(f"Removed: {queue.dequeue()}")
print(queue)
print(f"Length: {len(queue)}")

# print()
# print(f"Removed: {queue.dequeue()}") # This will throw an error as the queue is empty at this point
# print(queue)
# print(f"Length: {len(queue)}")
