from collections import deque

nums  = deque(input())
stack = deque()

for num in nums:
    if num.isdigit():
        stack.append(int(num))
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if num == "+":
            stack.append(num1+num2)
        elif num == "-":
            stack.append(num1-num2)
        elif num == "*":
            stack.append(num1*num2)
        else:
            stack.append(num1/num2)

print(stack.pop())