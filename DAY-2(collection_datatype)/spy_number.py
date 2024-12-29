# if sum of digits == product of digits
sum = 0
prod = 1
n = int(input())
while n > 0:
    rem = n % 10
    sum +=rem
    prod *= rem
    n = n//10
    
if sum == prod:
    print("spy")
else: 
    print("not spy")