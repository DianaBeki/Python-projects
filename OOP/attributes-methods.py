# attributes and methods
# attributes are pieces of data that are dyamic
# create objects
class PlayerCharacter:
    # class object attribute
    membership = True
    # constructor function
    def __init__(self, name, age): #dunder method, magicmethod
        if (self.membership):
        self.name = name # atrributes
        self.age = age
    
    def run(self):
        print('run')

player1 = PlayerCharacter('Cindy', 44) #call a class to create an object, which in this case is player1

play
player2 = PlayerCharacter('Tom', 22)

print(player1.membership) # True
print(player2.membership) # True