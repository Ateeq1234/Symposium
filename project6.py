from random import choice

questions= ['Why is the sky blue?','Why is there a face in the moon?'
,'Where have all the dinosaurs gone?']
print("Project-6")
print("_"*15)
question= choice(questions)
answer= input(question).strip().lower()

while answer != "just because":
    answer= input("why!:").strip().lower()

print("Oh.. okay")