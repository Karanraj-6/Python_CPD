#check armstrong number
n = int(input())
sum = 0
temp = n
digit = len(str(n)) 
while temp > 0:
    rem = temp % 10
    sum += rem ** digit
    temp = temp // 10
if sum == n:
    print("armstrong number")
else:   
    print("not armstrong number")
