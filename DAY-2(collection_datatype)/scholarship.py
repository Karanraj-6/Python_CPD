salary = int(input("Enter your salary :"))
if salary>=100000:
    tax = salary *(10/100)
    print(f"your tax in INR :{tax}")
elif salary< 100000 and salary >= 50000: 
    tax = salary *(5/100)
    print(f"your tax in INR :{tax}")
elif salary<50000 and salary >= 25000: 
    tax = salary *(2/100)
    print(f"your tax in INR :{tax}")
else:
    print("no tax") 
         