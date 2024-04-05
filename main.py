import random
comp=["Rock","Paper","Scissors"]
option=input("Do you want to play (y/n): ")
compoint=0
userpoint=0
while option.upper()=="Y":
    print("Computer: ",compoint,"Player: ",userpoint)
    print("-"*100)
    ran=random.choices(comp)
    ran=ran[0]
    user=input("enter your choice: ")
    user=user.title()
    print("Computer: ",ran)
    print("Player: ",user)
    if ran==user:
        continue
    elif ran=="Rock" and user=="Paper":
        userpoint+=1
    elif ran=="Rock" and user=="Scissors":
        compoint+=1
    elif ran=="Paper" and user=="Rock":
        compoint+=1
    elif ran=="Paper" and user=="Scissors":
        userpoint+=1
    elif ran=="Scissors" and user=="Rock":
        userpoint+=1
    elif ran=="Scissors" and user=="Paper":
        compoint+=1
    else:
        print("invalid input!!! please enter a valid value :)")
        option=="Y"

    if compoint==5 or userpoint==5:
        if compoint==5:
            print("Computer won!!")
            print("sorry!! better luck next time!!")
            op=input("try again? (y/n)")
            if op.upper()=="Y":
                compoint=0
                userpoint=0
                option="Y"
            else:
                print("See you again!!")
                break
        else:
            print("Congratulation!!! You won")
            op=input("try again? (y/n)")
            if op.upper()=="Y":
                compoint=0
                userpoint=0
                option="Y"
            else:
                print("See you again!!")
                break


