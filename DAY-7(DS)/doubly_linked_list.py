class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

N1=node(1)
N2=node(2)
N3=node(3)
N1.next=N2
N2.next=N3
N2.prev=N1
N3.prev=N2  

current=N1
while current:
    print(current.data,end="->")
    current=current.next

print()
print("Backward Traverse")

current=N3
while current:
    print(current.data,end="->")
    current=current.prev         