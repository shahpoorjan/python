userinput= input("Enter your car name? ").split()
emptylist=[]
for car in userinput:
    if car not in emptylist:
        emptylist.append(car)
print(emptylist)
