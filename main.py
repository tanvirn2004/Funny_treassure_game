print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/="._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First Mission
while True:
    first = input("Left or right?\nType Right/Left: ").lower()
    if first == "right":
        print('''
                      -     =    .--._
                - - ~_=  =~_- = - `.  `-.
              ==~_ = =_  ~ -   =  .-'    `.
            --=~_ - ~  == - =   .'      _..:._
           ---=~ _~  = =-  =   `.  .--.'      `.
          --=_-=- ~= _ - =  -  _.'  `.      .--.:
            -=_~ -- = =  ~-  .'      :     :    :
             -=-_ ~=  = - _-`--.     :  .--:    D
               -=~ _=  =  -~_=  `;  .'.:   ,`---'@
             --=_= = ~-   -=   .'  .'  `._ `-.__.'
            --== ~_ - =  =-  .'  .'     _.`---'
           --=~_= = - = ~  .'--''   .   `-..__.--.
             --==~ _= - ~-=  =-~_-   `-..___(  ===;
          --==~_==- =__ ~-=  - -    .'       `---'
  ''')
        print("Sonic got the treasure before you, try again.")
        continue
    elif first == 'left':
        print('''
   _                                                            
  | |                                                           
  | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
  | __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
  | |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
  \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                        | |    
                                                        |_| 
  ''')
        print("Nice, you made it to the next level!")
        break
    else:
        print("Invalid choice, try again.")

# Second Mission
while True:
    second = input("Your map shows that you need to get to Treasure Island, you can wait to board a ship or swim across the sea, pick one.\nType Swim/Wait: ").lower()
    if second == "swim":
        print('''
                    (`.
                    \ `.
                      )  `._..---._
    \`.       __...---`         o  )
    \ `._,--'           ,    ___,'
      ) ,-._          \  )   _,-'
    /,'    ``--.._____\/--''
        ''')
        print("Unfortunately, you were eaten by a Great White Shark, try again.")
        continue
    elif second == "wait":
        print("Nice, you made it to the next level, you're pretty good at this!")
        print ("Welcome to:")
        print ('''
     _                                     _     _                 _ 
    | |                                   (_)   | |               | |
    | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
    | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
    | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
    \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
    ''')
        break
    else:
        print("Invalid choice, try again.")

# Third Mission
while True:
    third = input("Now that you've made it to Treasure Island, you can dig or search the cave.\nType Dig/Cave: ").lower()
    if third == "dig":
        print("You've found the treasure, you win!")
        break
    elif third == "cave":
        print('''
      _                     
      | |                    
      | |__   ___  __ _ _ __ 
      | '_ \ / _ \/ _` | '__|
      | |_) |  __/ (_| | |   
      |_.__/ \___|\__,_|_|   
                  ''')
        print("You were eaten by a bear, game over.")
        continue
    else:
        print("Invalid choice, try again.")

print('''
    *******************************************************************************
    *                                                                             *
    *      Congratulations! You've successfully navigated through the obstacles   *
    *      and claimed the treasure of Treasure Island! You are now a true adventurer! *
    *                                                                             *
    *******************************************************************************
    ''')

# Final Mission - Escape the Island
while True:
    print("\nYou have found the treasure, but now you need to escape the island!")
    print("There are three possible ways to escape:")
    print("1. Take a boat.")
    print("2. Build a raft.")
    print("3. Wait for rescue.")

    choice = input("How would you like to escape? Type Boat/Raft/Wait: ").lower()
    if choice == "boat":
        print("\nThe boat was old and had holes. Unfortunately, it sank in the middle of the sea. Game over.")
    elif choice == "raft":
        print("\nYou successfully built a raft and sailed away to safety. Congratulations, you have fully completed the game!")
        break
    elif choice == "wait":
        print("\nYou waited for days, but no one came to rescue you. Game over.")
    else:
        print("Invalid choice, try again.")
        continue

print('''
    *******************************************************************************
    *                                                                             *
    *      You have escaped Treasure Island with the treasure! You are a true     *
    *      adventurer and have completed the entire journey. You win!             *
    *                                                                             *
    *******************************************************************************
    ''')

# Bonus Mission - Facing the Pirate Captain
while True:
    print("\nAfter escaping the island, you encounter a Pirate Captain who wants the treasure!")
    print("You have three choices to deal with the Pirate Captain:")
    print("1. Fight the Pirate Captain.")
    print("2. Offer half of the treasure.")
    print("3. Run away with the treasure.")

    choice = input("What do you want to do? Type Fight/Offer/Run: ").lower()
    if choice == "fight":
        print("\nYou fought bravely, but the Pirate Captain was too strong. Game over.")
    elif choice == "offer":
        print("\nThe Pirate Captain accepts half of the treasure and lets you go. You have survived!")
        break
    elif choice == "run":
        print("\nYou tried to run, but the Pirate Captain caught you. Game over.")
    else:
        print("Invalid choice, try again.")
        continue

# Epilogue
print('''
    *******************************************************************************
    *                                                                             *
    *      After a long and challenging journey, you managed to escape the Pirate *
    *      Captain and keep half of the treasure. You are a true adventurer, and  *
    *      your story will be remembered for generations.                         *
    *                                                                             *
    *******************************************************************************
    ''')

# Ultimate Challenge - The Hidden Temple
while True:
    print("\nAfter escaping the Pirate Captain, you discover a Hidden Temple deep in the jungle!")
    print("The temple is rumored to hold even greater riches, but it is protected by traps.")
    print("You have three choices:")
    print("1. Enter the temple carefully.")
    print("2. Set up camp and observe the temple for a day.")
    print("3. Ignore the temple and head home.")

    choice = input("What do you want to do? Type Enter/Observe/Ignore: ").lower()
    if choice == "enter":
        print("\nYou enter the temple and trigger a series of traps! Unfortunately, you couldn't escape them. Game over.")
    elif choice == "observe":
        print("\nAfter observing the temple for a day, you discover a hidden entrance that allows you to bypass the traps!")
        print("You enter the temple and find even more treasure, making you one of the richest adventurers ever!")
        break
    elif choice == "ignore":
        print("\nYou decide it's not worth the risk and head home with the treasure you already have. You win!")
        break
    else:
        print("Invalid choice, try again.")
        continue

# Final Success Message
print('''
    *******************************************************************************
    *                                                                             *
    *      You have completed the ultimate challenge and secured unimaginable     *
    *      wealth! Your name will go down in history as the greatest adventurer   *
    *      of all time. Congratulations on your success!                          *
    *                                                                             *
    *******************************************************************************
    ''')
