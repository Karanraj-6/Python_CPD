arr = list(map(int, input().split()))
stack = []
res = [-1]*len(arr)
for i in range(len(arr)):
    while stack and arr[stack[-1]]<arr[i]:
        index = stack.pop()
        res[index] = arr[i]
    stack.append(i)
print(res)