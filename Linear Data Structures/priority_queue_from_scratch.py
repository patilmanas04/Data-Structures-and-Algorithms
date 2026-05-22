class PriorityQueue:
    def __init__(self, capacity) -> None:
        self.queue = [0] * capacity
        self.front = self.rear = -1
        self.capacity = capacity
        self.count = 0

    def enqueue(self, value):
        if self.count == self.capacity:
            raise IndexError("queue has already reached its maximum capacity")
        if self.count == 0:
            self.rear = 0
            self.queue[self.rear] = value
            self.count += 1
            return
        i = self.rear
        while True:
            if i == self.front:
                break
            if self.queue[i] > value:
                next_idx = (i + 1) % self.capacity
                self.queue[next_idx] = self.queue[i]
                i = (i - 1) % self.capacity
            else:
                break
        insert_idx = (i + 1) % self.capacity
        self.queue[insert_idx] = value
        self.rear = (self.rear + 1) % self.capacity
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


queue = PriorityQueue(6)

queue.enqueue(1)
print(queue)
queue.enqueue(5)
print(queue)
queue.enqueue(7)
print(queue)
queue.enqueue(3)
print(queue)
queue.enqueue(6)
print(queue)
queue.enqueue(2)
print(queue)

print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
