# list =store multiple items in a single variable
food = ["pizza","burger","hotdog"]
drink = ["coc","pepsi"]
print(food)
print(food[0])

food[0]="bread"
for i in food:
    print(i)

food.append("ice cream")
print(food)
food.remove("burger")
print(food)
food.pop()
print(food)
food.insert(0,"cake")
print(food)
food.sort()
print(food)
food.clear()
print(food)

list = [True, False ]
print(list)

food.extend(drink)

print(food)