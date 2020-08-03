

def menu(list_ip):
    while(True):
        choice=input("enter your choice: \n1.create new file \n2.add new ip \n3.remove specific IP \n4.search specific IP \n5.print all IP ")
        if choice=="1":
            create_file()
        elif choice=="2":
            list_ip=add_ip(list_ip)
        elif choice=="4":
            search_ip(list_ip)
        else:
            print("enter 1-6 only!!!")
            continue
        if (input("Do you want to exit? y/n") == "y"):
            break
    print("thanks and bye bye...")


def create_file():
    print("creating new file... ")


def add_ip(list_ip):
    new_ip=search_ip(list_ip)
    if(new_ip!=False):
        print("adding new ip...")
        list_ip.append(new_ip)
        print("your new  list of ips: " + str(list_ip))
        return list_ip

def search_ip(list_ip):
    new_ip=input("enter ip: ")
    print("searching... ")
    if(new_ip in list_ip):
        print("this ip is already in use!")
        return False
    else:
        print("this ip is available")
        return new_ip




my_list=["192.168.1.1","1.1.1.1","55.55.55.55"]
menu(my_list)

