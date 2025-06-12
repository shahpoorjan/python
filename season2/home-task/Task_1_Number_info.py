number=int(input("Please enter your number to check if it is negative or positive and odd or even ? "))
if number == 0:
    print ("number is 0")
elif number < 0 and number % 2 == 0:
    print("number is negative and even")
elif number > 0 and number % 2 == 0:
    print ("number is positive and even")
elif number < 0 and number % 2 != 0:
    print("number is negative and odd")
elif number > 0 and number % 2 != 0:
    print ("number is positive and odd")







#     print ("number is negative")
#     if number % 2 == 0:
#         print ("number is negative and even")

# # elif number > 0:
# #     print ("number is negative")
# #     print ("Number is Negative and even")
# # elif number > 0 and number % 2 != 0:
# #     print (" Number is positive and odd")

# # elif number == 0:
# #     print("Number is 0 ")
# else:
#     print ("Number is positive and odd ")