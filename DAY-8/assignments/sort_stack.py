class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, data):  
        self.stack.append(data)

    def sort(self):
        self.stack.sort()

    def print(self):
        print(self.stack)

stack = Stack()
stack.push(10)
stack.push(40)
stack.push(20)
stack.push(50)
stack.sort()
stack.print() 