import random

class Pound:
    def __init__(self,rare=False):
        self.rare= rare
        if self.rare:
            self.value= 1.25
            self.color= "Gold"
        else:
            self.value= 1.00
            self.color= "Greenish"
        
        self.num_edges= 1
        self.diameter= 22.5 #mm
        self.thickness= 3.15 #mm
        self.heads= True

    def __del__(self):
        print("Coin Spent!")

    def clean(self):
        self.color= "Gold"

    def rust(self):
        self.color= "Greenish"

    def flip(self):
        heads_option= [True,False]
        choice= random.choice(heads_option)
        self.heads= choice
        # print(self.heads)

# coin1= Pound(rare=True)
coin2= Pound()
coin2.rust()
print(coin2.color,"After the coin has been rusted")
coin2.clean()
print(coin2.color, "After the coin has been cleaned")
# coin1.flip()
# print(coin1.heads)
# del coin2
