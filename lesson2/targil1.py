

def menu():
    while(True):
        choice=input("enter your choice: \n1.search specific IP \n2.delete specific IP \n3.add new IP \n4.print specific IP \n5.print all IP ")
        if choice=="1":
            first()
        elif choice=="2":
            second()
        elif choice=="3":
            third()
        elif choice=="4":
            fourth()
        elif choice=="5":
            fifth()
        else:
            print("enter 1-5 only!!!")
            continue
        if (input("Do you want to exit? y/n") == "y"):
            break
    print("thanks and bye bye...")


def first():
    search_ip=input("search an ip: ")
    if (search_ip in ip_add):
        print ("this ip exist!")
    else:
        ("this ip isn't exist!")

def second():
    del_ip = input("delete an ip address: ")
    ip_add.remove(del_ip)
    print(ip_add)

def third():
    add_ip=input("add new ip: ")
    ip_add.append(add_ip)
    print(ip_add)

def fourth():
    spec_ip=int(input("enter the IP in the list that you want to see acorrding to his order:  "))
    print(ip_add[spec_ip-1])

def fifth():
    print(ip_add)






ip_add=[]
for i in range(6):
    ip_add.append(input("enter ip: "))
    print(ip_add)
menu()





