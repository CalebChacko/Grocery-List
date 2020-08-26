
class GroceryList:
    items = {}

    def CompareRecipeToPantry(self, recipeBook, pantry, weekSchedule, groceryList):
        for recipe in weekSchedule.recipes:
            #print(recipeBook.recipes[recipe].ingredients, '\n')
            for key in recipeBook.recipes[recipe].ingredients.keys():
                #print("Ingredient: ", key)
                if pantry.ingredients.get(key, 'null') == 'null':
                    #print(key, "needs to be added")
                    groceryList.items[key] = "Welcome"

    def print(self):
        print("--- Today's Grocery List ---")
        for key in self.items:
            print(key)
