# integernumber= int(input(" enter your float number? "))
# print(int(integernumber))

year = int(input("please enter the year to check if it is a leap year or not : "))
if year % 4 == 0 or year % 400 == 0:
    print (f"the {year} is leap year!")
elif year % 4 == 0 and year % 100 == 0: 
    print ("it is not a leap year ")
else:
    print ("its not a leap year")