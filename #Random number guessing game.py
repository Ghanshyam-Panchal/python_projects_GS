##Random number guessing game
# using random modeul

# import random
# Cnumber=random.randrange(1,101)
# userInput=int(input("Enter your number:---"))
# if userInput>Cnumber:
#     print("Computer Number",Cnumber)
#     print("Your guess number is too high")
# elif Cnumber>userInput:
#     print("Computer Number",Cnumber)
#     print("Your guess number is too low")
# else:
#     print("Computer Number",Cnumber)
#     print("Your guess number is equal")

# ############################################
# Project
# Rock paper scissors game
# Using random Module
import random
l=["Rock","Scissor","Paper"]

'''
Rock vs paper -> paper wins
Rock vs sciessor -> Rock wins
Paper vs Scissor -> Scissor wins
'''
while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game statrt..............
1 Yes
2 No | Exit
'''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1. Rock
2. Sciessor
3. Paper
'''))
            if userInput==1:
                uchoice="Rock"
            elif userInput==2:
                uchoice="Scissor"
            elif userInput==3:
                uchoice="Paper"
            Cchoice=random.choice(l)
            if   Cchoice==uchoice:
             print("Computer value",Cchoice)
             print("User value",uchoice)
             print("Game draw") 
            ucount=ucount+1
            ccount=ccount+1

    elif(uchoice=="Rock" and Cchoice=="Scissor") or (uchoice=="Paper" and Cchoice=="Rock") or (uchoice=="Scissor" and Cchoice=="Paper"): 
             print("Computer value",Cchoice)
             print("User value",uchoice)
             print("You win")
             ucount=ucount+1
    else:
             print("Computer value",Cchoice)
             print("User value",uchoice)
             print("Computer win")
             ccount=ccount+1

    if ucount==ccount:
         print("Final Game draw..")
         print("User score",ucount)
         print("Compuer count",ccount)

    elif ucount>ccount:   
         print("You win the Game")
         print("User score",ucount)
         print("Compuer count",ccount)  

    else:
         print("Compuer win the Game")
         print("User score",ucount)
         print("Compuer count",ccount)     


else:
     endingend
     
     
     