from recipe import Recipe

class RecipeBook:
    recipes = {}
    name = "Jim"


    def addRecipe(self, name):
        newRecipe = Recipe(name)
        newRecipe.name = name
        print("Add an ingredient and press enter. If finished type in '---' and enter")
        ingredient = ""
        while ingredient != "---":
            ingredient = input()
            if ingredient != "---":
                newRecipe.addIngredient(ingredient)

        self.recipes[newRecipe.name] = newRecipe

    def deleteRecipe(self, name):
        del self.recipes[name]
        print("Deleted", name)

    def searchRecipe(self, name):
        if self.recipes.get(name, 'null') != 'null':
            return bool(1)

