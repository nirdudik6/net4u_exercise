


budget=int(input("enter your total budget(Dollar): "))
facebook=int(input("how long facebook campagin will run? "))
instagram=int(input("how long intagram campagin will run? "))
sum=((facebook*100) + (instagram*50))
#sum2=(int(sum*1.17*3.5))
print("\nsum with fee: " + str(sum) + " $")
#print("\nsum with fee: " + str("%.1f" % (sum*1.17*3.5)) + " NIS")
if (budget >= sum):
    print("successfull and you have got: " + str(budget-sum) + " $")
else:
    print("the price is too expensive you have to add: " + str(sum-budget) + " $")