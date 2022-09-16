import random
import time
def gamewin(comp,user):
    if comp==user:
        return None
    elif comp=='s':
        if user=='w':
            return False
        elif user=='g':
            return True
    elif comp=='w':
        if user=='g':
            return False
        elif user=='s':
            return True
    elif comp=='g':
        if user=='s':
            return False
        elif user=='w':
            return True

print("~~~~~Let's Play a game~~~~")
print("---------------------")
print("Name of game is Snake , Water and Gun ")
print("---------------------")
print("Computer chooses Snake, Water or Gun Randomly")
print("---------------------")
print("Press q for quite.")
print("---------------------")
print("You are here means you want to Play...")
choice=True
while(choice):
    i=0
    comscore=0
    userscore=0
    while(i!=10):
        randno=random.randint(1,3)
        if randno==1:
            comp ='s'
        elif randno==2:
            comp ='w'
        else:
            comp ='g'
        print("---------------------")
        user=input("Enter s ,w or g: ")
        if user.lower()=='s' or user.lower()=='w' or user.lower()=='g':
            print("---------------------")
            i=i+1
            win=gamewin(comp,user)
            print("Computer choose: ",comp)
            if(win==None):
                print("No one Wins. Try Again.")
            elif win:
                comscore=comscore+1
                print ("You win.")
            else:
                userscore=userscore+1
                print("You lose")
        elif user.lower()=='q':
            print("Do you want to exit?")
            print("-----------------------")
            confirm=input("Press y for yes or n for no : ")
            if confirm.lower()=='y':
                print("-----------------------")
                print("Thanks For choosing Central Library.")
                print("-----------------------")
                time.sleep(2)
                exit()
        else:
            print("Invalid Choice.")

    print(f"Computer Score is {comscore}.")
    print(f"User Score is {userscore}.")
    if comscore==userscore:
        print("Game Tied.")
    elif comscore<userscore:
        print("Congratulation!! You Win.")
    else:
        print("Computer Wins. Try Again.")
    print("-----------------------")
    print("DO you want to Play Again?")
    while(True):
        choice=input("Press Y for Yes and N for No : ")
        if choice.lower()=='n' or choice.lower()=='y':
            if choice.lower()=='n':
                print("-----------------------")
                print("Thanks For Playing this Game.")
                print("-----------------------")
                time.sleep(2)
                exit()
            else:
                break
        else:
            print("-----------------------")
            print("Invalid Choice.")

        

