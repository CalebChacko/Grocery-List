
class Recipe:
    name = 'None'

    ingredients = {}

    # Determines if we add/remove ingredient on update
    addIngredients = bool(0)

    def __init__(self, name):
        self.name = name

    def addIngredient(self, newIngred):
        print(len(self.ingredients))
        self.ingredients[(len(self.ingredients)+1)] = newIngred
        print("I'm adding ingredients")

    def removeIngredients(self):
        print("I'm removing ingredients")

    def updateIngredients(self, addIngredients):
        print ("I'm", addIngredients)


