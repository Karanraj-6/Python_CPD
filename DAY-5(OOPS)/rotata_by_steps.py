n = int(input())
nums = list(map(int,input().split()))
k = int(input())
for i in range(k):
    nums.append(nums[0])
    nums.pop(0)
print(nums)

print("another method")


for i in range(k+1):
    nums.insert(0,nums.pop())
    print(f"After iteration {i + 1}: {nums}")
print(nums)




for i in range(k + 1):
    nums.insert(0, nums.pop())  # Pop the last element and insert it at the start
    print(f"After iteration {i + 1}: {nums}")

print(f"Final rotated list: {nums}")