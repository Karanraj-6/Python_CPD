n = int ( input ( "Enter number : "))

if ( n<=1 ):
    print("Not Prime number")
for i in range (1,n+1):
    count = 0
    for j in range (1, i+1):
        if ( i % j == 0):
            count +=1
    if (count == 2):
        print(f"{j} prime number")
   

    
