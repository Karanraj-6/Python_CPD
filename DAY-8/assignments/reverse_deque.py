from collections import deque

nums = deque(map(int, input().split()))
# nums.reverse()
while nums:
    print(nums.pop(), end=" ")