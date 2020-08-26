from ingredient import Ingredient

class Pantry:
    name = "Joe"

    ingredients = {}

    def addIngredients(self):
        print("Add each ingredient to the pantry by typing the name and pressing enter.\n"
              "If finished type in '---' and enter\n")
        ingredName = ""
        while ingredName != "---":
            ingredName = input()
            if ingredName != "---":
                self.ingredients[ingredName] = Ingredient(ingredName)

    def deleteIngredients(self):
        print("Delete each ingredient from the pantry by typing the name and pressing enter.\n"
              "If finished type in '---' and enter \n")
        ingredName = ""
        while ingredName != "---":
            ingredName = input()
            if (self.ingredients.get(ingredName, 'null') != 'null') and (ingredName != "---"):
                del self.ingredients[ingredName]