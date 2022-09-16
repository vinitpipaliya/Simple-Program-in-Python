import random
import time

print("----------------")
print("Lets play a Game!!")
print("I am picking a number berween 1 to 100.")
print("You have to guesss which number I guessed.")
print("----------------")
choice=True
while(choice):
    randNumber=random.randint(1,100)
    guess=0
    user=None
    while(randNumber!=user):
        try:
            user=int(input("Enter a number: "))
            print("----------------")
            guess+=1
            if user==randNumber:
                print("****You guessed Correct Number!****")
            else:
                if user>randNumber:
                    print("You guessed wrong number. Enter smaller number :")
                else:
                    print("You guessed wrong number. Enter larger number : ")
        except Exception as e:
            print("Invalid Choice.")

    print(f"You guess correct number in '\033[1m{guess}\033[0m' guess.") #--> For printing guess value in Bold.
    try:
        with open("hiscore.txt")as f:
            hiscore=int(f.read())
        if guess<hiscore:
            print("Congratulation!! You created Highscore.")
            with open("hiscore.txt","w") as f:
                f.write(str(guess))
    except Exception as e:
        None
    print("----------------")
    print("Do you want to play again?")
    print("----------------")
    while(True):
        choice=input("Press y for yes and n for no :")
        print("----------------")
        if choice.lower()=='y' or choice.lower()=='n':
            if choice.lower()=='n':
                print("Thnaks For Playing this Game.")
                print("----------------")
                time.sleep(2)
                exit()
            else: 
                break
        else:
            print("Invalid Choice.")
            print("----------------")

