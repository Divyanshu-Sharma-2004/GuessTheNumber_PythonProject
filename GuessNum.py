import random

target = random.randint(1,100)
score = 11
chance = 0

print("---------Welcome In Guess Game---------")
print("Rules :- given below")
print("1.You have to guess the correct number")
print("2.You have 10 chances to guess the correct number")
print("3.You will get score after winning , score as much you can")
print("Lets begin :-")
while True:
    
    userChoice = input("Guess the number or quit(Q): ")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    score -= 1
    chance += 1
    
    if(userChoice ==  target):
        print("Success : correct Guess")
        break

    if(userChoice <= target - 15 and userChoice < target - 10):
        print("your number is too small. Think big and guess again")
    elif(userChoice >= target + 15 and userChoice > target + 10):
        print("your number is too big. Think small and guess again")
    elif(userChoice < target):
        print("The guess is small but you are so close. keep guessing")
    elif(userChoice > target):
        print("The guess is big but you are so close. keep guessing")

    if(chance == 10):
        break

if(userChoice != "Q" and userChoice ==  target):
    print("Your score is",score,"/ 10")
if((userChoice == "Q" or chance == 10) and userChoice !=  target):
    print("You losses ):")
print("--------Game over--------")