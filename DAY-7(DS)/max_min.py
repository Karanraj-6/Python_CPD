nums = list(map(int,input().split()))
max=nums[0]
min=nums[0]
for i in nums:
    if i>max:
        max=i
    if i<min:
        min=i
print(max)
print(min)