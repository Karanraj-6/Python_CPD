no = int(input())
n = list(map(int,input().split()))

for i in range(no):
    for j in range(i+1,no):
        if n[j]<n[i]:
            n[i],n[j] = n[j],n[i]
print(n)
    