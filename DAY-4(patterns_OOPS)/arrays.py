arr = [1,2,3,4,5]
print(arr[::-1])

lenght = len(arr)
while lenght > 0:
    print(arr[lenght - 1],end="")
    lenght-=1