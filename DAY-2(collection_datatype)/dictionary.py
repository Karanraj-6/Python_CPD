# dictionary = A changeable, unordered collection of unique key
#             :value pair fast because they use hashing ,allow us to access a value quickly 

capitals={'USA':'waShington','INDIA':"new delhi",
          'CHINA':'beijing',"RUSSIA":'MOSCOW'}

print(capitals)
print(capitals['RUSSIA'])
print(capitals.get('INDIA')) #get returns none where there is no key
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({'germany':'berlin'})
capitals.pop('CHINA')

for key,value in capitals.items():
    print(key,value)
capitals.clear()
print(capitals)
capitals['INDIA']='Mumbai'
print(capitals)