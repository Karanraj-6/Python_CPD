
dict1 = {
    "A":1,
    "B":2,
    "C":3
}

print(dict1)

# udpate
dict1.update({"D":4})
print(dict1)

# delete
del dict1["A"]
print(dict1)

#pop   
dict1.pop("C")
print(dict1)

#copy
dict2 = dict1.copy()
print(dict2)

#keys
print(dict1.keys()) 

#values     
print(dict1.values())

#items
print(dict1.items())

#clear
dict1.clear()
print(dict1)