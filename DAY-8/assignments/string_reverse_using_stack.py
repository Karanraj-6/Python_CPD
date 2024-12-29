# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, data):
#         self.stack.append(data)

#     def pop(self):
#         if not self.stack:
#             return None
#         return self.stack.pop() 

#     def is_empty(self):
#         return not bool(self.stack) 

#     def reverse_string(self, string):
#         for char in string:
#             self.push(char)
#         reversed_string = ""
#         while not self.is_empty():
#             reversed_string += self.pop()
#         return reversed_string
    

# stack = Stack() 
# print(stack.reverse_string("Hello")) 
# print(stack.reverse_string("World"))  



#another method

input= list(map(int,input().split()))
res = []
while input:
    curr=input.pop()
    while res and res[-1]>curr:
        input.append(res.pop())
    res.append(curr)
print(res)
