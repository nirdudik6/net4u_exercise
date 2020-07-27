

def menu(ip_add):
    while(True):
        choice=input("enter your choice: \n1.search specific IP \n2.delete specific IP \n3.add new IP \n4.print specific IP \n5.print all IP ")
        if choice=="1":
            first()
        elif choice=="2":
            ip_add=second(ip_add)
        elif choice=="3":
            ip_add=third(ip_add)
        elif choice=="4":
            ip_add=fourth(ip_add)
        elif choice=="5":
            ip_add=fifth(ip_add)
        else:
            print("enter 1-5 only!!!")
            continue
        if (input("Do you want to exit? y/n") == "y"):
            break
    print("thanks and bye bye...")


def first(ip_add):
    search_ip=input("search an ip: ")
    if (search_ip in ip_add):
        print ("this ip exist!")
        return False
    else:
        ("this ip isn't exist!")
        return search_ip
def second():
    del_ip = input("delete an ip address: ")
    ip_add.remove(del_ip)
    print(ip_add)

def third(ip_add):
    add_ip= first(ip_add)
    if(add_ip!=False):
        print("adding new ip...")
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
menu(ip_add)





