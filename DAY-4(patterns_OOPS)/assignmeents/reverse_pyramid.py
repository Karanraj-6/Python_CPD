#reverse pyramid
def reverse_pyramid(n):
    for i in range(n,0,-1):
        print(" "*(n-i),end="")
        print("*"*(2*i-1))
        
reverse_pyramid(5)