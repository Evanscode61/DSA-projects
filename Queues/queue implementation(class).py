#Queue implementation using python list
class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, item):
        if len(self.queue) == self.size:
            print("Queue is full")
        else:
            self.queue.append(item)
            print(f"{item} added to queue")
# To remove an item from the list
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print(f"{self.queue.pop(0)} removed from queue")
# To display the front element
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    def display(self):
        print("Queue:", self.queue)



q = Queue(3)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.peek()
