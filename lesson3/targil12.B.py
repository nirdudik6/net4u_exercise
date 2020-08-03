def total_cube(n):
    n=n-1
    sum=0
    while(n > 0):
        sum=sum+(n**3)
        n=n-1
    return sum

print(total_cube(int(input("enter a number:"))))