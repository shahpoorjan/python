import time

print("The Game is starting..")
time.sleep(1)
print("1..")
time.sleep(2)
print("2...")
time.sleep(2)
print("3... lets start")
time.sleep(1)
player1= input("Player 1 : enter rock , paper or scissors ? ")
player2= input("Player 2: enter rock , paper or scissors ? ")

time.sleep(2)
print ("please wait for the result...")
time.sleep(2)
if player1 == "rock" and player2 == "scissors":
    print ("Player1 won")

elif player1 == "paper" and player2 == "rock":
        print ("Player1 won")
elif player1 == "scisoors" and player2 == "paper":
        print ("Player1 won")
elif player1 == player2:
    print("its a tie")
else:
    print("player2 Won")