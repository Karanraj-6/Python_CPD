# functions are block of code which performs a specific task
# def keyword is used to define the function
# function name should be in lowercase
# function name should be meaningful
# function name should be unique
# function name should be short
# function name should be readable
# function name should be specific
# function name should be reusable

#syntax
# def function_name():
#     statements


def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b


print(addition(2,3))
print(subtraction(2,3)) 
print(multiplication(2,3))
print(division(2,3))



def check_even_odd(a):
    if (a % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(check_even_odd(2))


def check_prime(n):
    count = 0
    for i in range (1, n+1):
        if ( n % i == 0):
            count +=1
        
    if (count == 2):
        return 1
    else:
        return 0


print(check_prime(2))