from collections import deque

n = int(input())

nums = deque()
for i in range(1,n+1):
    nums.append(bin(i))

while nums:
    print(nums.popleft(), end=" ")
    
    
# another method

from collections import deque

# queue = deque()
# result = []
# queue.append(1)
# n = 