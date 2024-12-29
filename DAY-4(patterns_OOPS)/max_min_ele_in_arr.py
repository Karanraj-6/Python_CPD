a = [1,2,3,4,5]

print(max(a))
print(min(a))

print("\n")

max_ele=a[0]
min_ele=a[0]

for i in a:
    if i>max_ele:
        max_ele=i
    if i<min_ele:
        min_ele=i

print(max_ele)
print(min_ele)