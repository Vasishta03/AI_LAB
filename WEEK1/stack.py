class Stack:
    def push(self, item):
        self.items.append(item)
    def __init__(self):
        self.items = []
    def pop(self):
        return self.items.pop() if self.items else None
    def is_empty(self):
        return not self.items
    def peek(self):
        return self.items[-1] if self.items else None
    

class Queue:
    def enqueue (self, item):
        self.stack1.push(item)
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    def dequeue (self):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        ret = self.stack2.pop()
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())
        return ret
    def is_empty(self):
        return self.stack1.is_empty()


que = Queue()
que.enqueue(5)
que.enqueue(3)
que.enqueue(4)
que.enqueue(2)
print(que.dequeue())
print(que.dequeue())


#output: 5
#3