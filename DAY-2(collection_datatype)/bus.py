gender = input("Enter your gender :")
belong = input("Enter your belong :")
id = bool(input("carrying id (enter true/false):"))

if(gender.lower() == 'female' and id == True):
    if belong.lower() == 'telangana':
        print("free ride")
    elif belong.lower() == 'andhrapradesh':
        print("50 percent off free ride")
    else:
        print("not free ride") 
else:
    print("not free ride")
         