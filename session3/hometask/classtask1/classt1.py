# iterator = variable used within loop value of which changes based on the sequence
# 

# inp = input(" input word : ")
# inp2= input(" input a charector: ") 
# for char in inp:
#     if char == inp2:
#         print(char)

# inp1= input("input a word: ") 
# inp2= input(" input a charector: ")
# counter =0
# for char in inp1:
#     if char == inp2:
#         counter +=1
# print (counter)
# inp= int(input("input: "))

# for number in range(inp):
#     if number %2 == 0:
#         print(number)


#while loop
# unlike for loop while does not have start point or end


# # while loops are based on conditions and if the condition is true it runs it again and again until false
# while <condition>:
#     code

# inp= int(input("input: "))
# start=4
# while start < inp:
#     print(start)
#     start +=1

# break and contiue only used with loops
# task:


# Lists | tuple| dictionary |sets cand are data type that can hold from 0  or more values
# list is a data type that can hold 0 or more values
#list starts with []
# lst = ["hello" , "ahmad" , 10 , True,  ["hello" ,"test"]]
# print(lst [1][2])


# while <condition>:
#         do_somthing
#         do_something2

# counter=1
# while counter > 15:
#         print(counter)
#         counter +=1
# print("finished")
sec_num= 12
user_inp=int(input("guese the sec number ? "))
while user_inp != sec_num:
        print("worng guese")
        user_inp=int(input("guese the sec number ? "))
print("perfect")
