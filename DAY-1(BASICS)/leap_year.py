
n = int ( input ("Enter year:"))


if ( n % 400 == 0 and n % 100 == 0) or ( n % 100 !=0 and n%4==0):
    print("Leap year")
else:
    print("not a Leap year")