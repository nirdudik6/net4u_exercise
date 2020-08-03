

def product(number):
    for i in range(len(number)):
        for j in range(len(number)):
            if i != j:
                 product = number[i] * number [j]
                 if product & 1:
                     return True
                     return False



dict1=[2,4,6,8]
dict2=[1,6,4,7,8]
print(dict1,product(dict1))
print(dict2,product(dict2))
