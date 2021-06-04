# Project - 04  
# Shows the usage of conditional statements

known_users= ['Tom','Jerry','doraemon','Shinchan','ben','kevin','carryminati']
print(known_users)

# print(len(known_users))

while True:
    print("Hi I am Travis")
    name = input("May I know your name please").strip()

    if name in known_users:
        print("Hello "+name)
        print(known_users)
        remove= input("Would you like to be removed(Y/N)\n").strip().lower()
        if(remove=="y"): 
            known_users.remove(name)
            print(known_users)

        elif(remove== "n"):
            print("No problem I didn't want you to be removed")
            
    else:
        print("Your name is not recognized")
        added= input("would you like to be added (y/n)\n").strip().lower()
        if added== "y":
            known_users.append(name)
        elif added == "n":
            print("Have a good day")

    