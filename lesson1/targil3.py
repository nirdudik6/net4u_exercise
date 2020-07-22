

def menu():
    while(True):
        choice=input("enter your choice: \n1.search ip address \n2.add ip address \n3.delete ip address \n4.print all the ip in the list ")
        if choice=="1":
            first()
        elif choice=="2":
            second()
        elif choice=="3":
            third()
        elif choice=="4":
            fourth()
        else:
            print("enter 1-4 only!!!")
            continue
        if (input("Do you want to exit? y/n") == "y"):
            break
    print("thanks and bye bye...")


def first():
    look_ip=input("enter an ip: ")
    if (look_ip in ip_add):
        print("this ip exists!")
    else:
        print("this ip isn't exists!")

def second():
    new_ip=input("add new ip address: ")
    ip_add.append(new_ip)
    print(ip_add)

def third():
    del_ip=input("delete an ip address: ")
    ip_add.remove(del_ip)
    print(ip_add)

def fourth():
    print(ip_add)







ip_add=[]
for i in range(6):
    ip_add.append(input("enter new ip: "))
    print(ip_add)
menu()




