a = [1,2,4,2,4,4,6,7,5]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)