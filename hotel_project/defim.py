
def menu():
    choice = input("enter your choice: \n1.show availabe rooms \n2.search date \n3.order a room \n4.cancel an order \n5.search order and print the order ")
    if (choice == "1"):
        show_rooms()
    elif (choice == "2"):
        search_date()
    elif (choice == "3"):
        order_room()
    elif (choice == "4"):
        cancel_order()
    elif (choice == "5"):
        search_print()
    else:
        print("enter 1-5 only!!")


def show_rooms():
    hotel=input("enter the hotel: ")
    if (hotel == "setai"):
        setai = "C:/Users/User/Desktop/hotels/setai.txt"
        file = open(setai, "r")
        print(file.read())
    elif (hotel == "herodes"):
        herodes = "C:/Users/User/Desktop/hotels/herodes.txt"
        file = open(herodes, "r")
        print(file.read())
def search_date():
    day = input("enter a day you want to check:  ")
    if (day == "sunday"):
        setai ="C:/Users/User/Desktop/hotels/setai.txt"
        file = open(setai, "r")
        print("setai:")
        print(file.readlines()[0])
        herodes = "C:/Users/User/Desktop/hotels/herodes.txt"
        file = open(herodes, "r")
        print("herodes:")
        print(file.readlines()[0])
    elif (day == "monday"):
        setai ="C:/Users/User/Desktop/hotels/setai.txt"
        file = open(setai, "r")
        print("setai:")
        print(file.readlines()[1])
        herodes = "C:/Users/User/Desktop/hotels/herodes.txt"
        file = open(herodes, "r")
        print("herodes:")
        print(file.readlines()[1])
    elif (day == "tuesday"):
        setai ="C:/Users/User/Desktop/hotels/setai.txt"
        file = open(setai, "r")
        print("setai:")
        print(file.readlines()[2])
        herodes = "C:/Users/User/Desktop/hotels/herodes.txt"
        file = open(herodes, "r")
        print("herodes:")
        print(file.readlines()[2])
    elif (day == "wednesday"):
        setai ="C:/Users/User/Desktop/hotels/setai.txt"
        file = open(setai, "r")
        print("setai:")
        print(file.readlines()[3])
        herodes = "C:/Users/User/Desktop/hotels/herodes.txt"
        file = open(herodes, "r")
        print("herodes:")
        print(file.readlines()[3])
    elif (day == "thoursday"):
        setai ="C:/Users/User/Desktop/hotels/setai.txt"
        file = open(setai, "r")
        print("setai:")
        print(file.readlines()[4])
        herodes = "C:/Users/User/Desktop/hotels/herodes.txt"
        file = open(herodes, "r")
        print("herodes:")
        print(file.readlines()[4])

def order_room():
    hotel=input("which hotel do you want to order? ")
    if (hotel == "setai"):
        print("welcome to setai hotel!")
        setai = "C:/Users/User/Desktop/hotels/setai.txt"
        file = open(setai, "r")
        print("this is the available days:")
        print(file.read())
        cii = str(input("Check-In: "))



def cancel_order():
    h

def search_print():
    h






