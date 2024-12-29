class queue:
    def __init__(self):
        self.queue=[]   
    def enqueue(self,data):
        self.queue.append(data) 
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue)==0
    def remove_nth(self,n):
        if self.is_empty():
            return None
        for i in range(n):
            self.dequeue()
        return self.dequeue()
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.remove_nth(2)) #Output: 30