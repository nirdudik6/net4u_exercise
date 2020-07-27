
def menu():
    while(True):
        choice=input("enter your choice: \n1.search url \n2.add url+ip address \n3.delete url \n4.update ip address \n5.print all ")
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
    look_url=input("enter an url: ")
    if (look_url in dict):
        print("this url exists!")
    else:
        print("this url isn't exists!")


def second():
    print("add another url and ip: ")
    dict.update({input("add new url"): input("add new ip address")})
    print("adding the url and ip... ")
    print(dict)

def third():
    del_url=input("enter the url you want to delete: ")
    dict.pop(del_url)
    print(dict)

def fourth():
    update_ip=input("enter a new ip: ")
    current_url=input("enter an exist url: ")
    dict.update({(current_url):(update_ip)})
    print(dict)


def fifth():
    print(dict)





dict={}
for i in range(6):
    dict.update({input("add url"):input("add ip address")})
    print(dict)
menu()
