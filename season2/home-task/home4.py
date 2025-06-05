# # age = int(input("Enter your age: "))
# # if age >= 18 and age < 65:
# #     print("You are an adult.")
# # else:
# #     print(" ur input is not in range")
# import random
# random_n= random.randint(1,10)
# usernum=int(input("please provid a random number between (0,10) ? " ))
# if usernum < random_n:
#     print (" number is too low")
# elif usernum > random_n:
#     print ("number is too high")
# elif usernum == random_n:
#     print ("correct")
# else:
#     print ( " your number is out of range try again ... ")
import time
import random
rndn= random.randint(1,10)
print ("Are you ready ...? ")
time.sleep(3)
print ("The Random number game starts now .. ")
time.sleep (2)
usernumber= int(input("Enter your number between (1-10 ? "))
if usernumber > rndn:
    print ( "oh nooo... your number is too high ..")
elif usernumber < rndn:
    print("oh noo.. your number is too low haha ")
elif usernumber == rndn:
    print ("You Got it Congratss.. you guesed the correct number.")
    