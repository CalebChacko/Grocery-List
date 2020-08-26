import click
from recipe import Recipe

class Manager:

    def RecipeBookManager(self, recipeBook, recipeAction):
        recipeBook.name = "A Whole New World"
        if recipeAction == "add":
            name = click.prompt("What's the recipe name")
            recipeBook.addRecipe(name)
        elif recipeAction == "delete":
            name = click.prompt("What's the recipe name")
            recipeExists = recipeBook.searchRecipe(name)
            if recipeExists:
                recipeBook.deleteRecipe(name)
            else:
                print("Could not find recipe")
        elif recipeAction == "update":
            # This could be a little more complex
            print("Update recipe ingredients (feature coming soon")
        elif recipeAction == "search":
            name = click.prompt("What's the recipe name")
            recipeExists = recipeBook.searchRecipe(name)
            if recipeExists:
                print("Found recipe")
            else:
                print("Could not find recipe")

    def PantryManager(self, pantry, pantryAction):
        if pantryAction == "add":
            pantry.addIngredients()
        elif pantryAction == "delete":
            pantry.deleteIngredients()
        elif pantryAction == "clear":
            print("Clear all ingredients (feature coming soon)")
            #isVerified = click.prompt("Are you sure you want to clear? [y]/[n]")

    def ScheduleManager(self, schedule, scheduleAction):
        if scheduleAction == "add":
            schedule.addRecipes()
        elif scheduleAction == "delete":
            schedule.deleteRecipes()
        elif scheduleAction == "print":
            schedule.printRecipes()

    def GroceryListManager(self, recipeBook, pantry, schedule, groceryList, gLAction):
        if gLAction == "print list":
            groceryList.CompareRecipeToPantry(recipeBook, pantry, schedule, groceryList)
            groceryList.print()