'''
Project-5
Cinema Simulator
'''

films={
    'Tarzan':[15,2],
    'Tom and jerry':[15,5],
    'Avengers':[10,5],
    'The dark Knight':[10,5]
}

print("Project-5")
print("_"*15)

while True:
    choice= input("Enter the film you want to watch?\n").strip().title()
    if choice in films:
        age=int(input("How old are you:").strip())
        if age >= films[choice][0]:
            nums_seat= films[choice][1]
            if nums_seat>0:
                print("Ok your Request is granted, Enjoy the filEnjoy the film")
                films[choice][1] =films[choice][1]- 1

            else:
                print("Sorry we are sold out")
        else:
            print("You are underage\n")

    else:
        print("We don't have that film")
    
