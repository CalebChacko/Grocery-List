
class Schedule:
    weekOf = "Sept 4"
    recipes = {}

    def addRecipes(self):
        print("Add recipe to this week's schedule by typing the name and pressing enter.\n"
              "If finished type in '---' and enter \n")
        recipe = ""
        while recipe != "---":
            recipe = input()
            if recipe != "---":
                self.recipes[recipe] = 1

    def deleteRecipes(self):
        print("Delete recipe from this week's schedule by typing the name and pressing enter.\n"
              "If finished type in '---' and enter \n")
        recipe = ""
        while recipe != "---":
            recipe = input()
            if (self.recipes.get(recipe, 'null') != 'null') and (recipe != "---"):
                del self.recipes[recipe]

    def printRecipes(self):
        print(self.ingredients)