from ingredient import Ingredient

class Recipe:
    name = 'None'

    ingredients = {}

    # Determines if we add/remove ingredient on update
    addIngredients = bool(0)

    def __init__(self, name):
        self.name = name

    def addIngredient(self, newIngred):
        self.ingredients[newIngred] = Ingredient()
        print("I'm adding ingredients")

    def removeIngredients(self):
        print("I'm removing ingredients")

    def updateIngredients(self, addIngredients):
        print ("I'm", addIngredients)

    def print(self):
        print(self.ingredients)


