# inp= input("input a word : ")
# inp2=input("input a letter ? ")
# counter = 0
# for i in inp:
#     if i == inp2:
#         counter += 1
# print(counter)inp=input("provide the secret name or exit:")
inp1 =int(input("guese the secret number? "))
secret= 5
while True:
    if inp1 > 5:
        print("too high! ")
    else:
        print("too low")
    inp1 =int(input("try again? "))
print("perfect guese")