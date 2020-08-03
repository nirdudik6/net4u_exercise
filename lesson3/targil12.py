

def total_cube(n):
    sum=0
    for i in range(1,n):
        sum=sum+i**3
    return sum

print(total_cube(int(input("enter a number:"))))




