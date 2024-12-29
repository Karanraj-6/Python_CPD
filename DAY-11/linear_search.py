arr = [3,2,5,6]
target = 5
index = -1
for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break
    
print(f"index: {i}")
    