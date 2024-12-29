n = int(input())
n = str(n)
m= n[::-1]
r = int(m)

print(n)
print(r)

if n == r:
    print("palindrome")
else:
    print("not palindrome")