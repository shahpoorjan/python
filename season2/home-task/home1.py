
age= int(input(" please enter your age to check it ? "))
if age >= 18:
    if age >= 65:
        print(" you are sinior")
    else:
        print ("your are adult")
elif age < 18 and age > 0:
    print (" your are  a minor")
else:
    print ( " your input is out our range ")