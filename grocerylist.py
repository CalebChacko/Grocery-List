import click
from recipe import Recipe
from recipebook import RecipeBook
from pantry import Pantry
from schedule import Schedule
from taskmanager import Manager

cookBook = RecipeBook()
housePantry = Pantry()
weekSchedule = Schedule()

manager = Manager()

@click.command()
@click.option("--target", prompt=True, help="Add to target location")
@click.option("--action", prompt=True, help="Add to target location")
def main(target, action):
    cookBook.name = "This is mine"
    if target == 'recipe':
        #manager.RecipeBookManager(cookBook, action)
        #print("The cookbook name is", cookBook.name)
        if action == "add":
            name = click.prompt("What's the recipe name")
            cookBook.addRecipe(name)
        elif action == "delete":
            name = click.prompt("What's the recipe name")
            recipeExists = cookBook.searchRecipe(name)
            if recipeExists:
                cookBook.deleteRecipe(name)
            else:
                print("Could not find recipe")
        elif action == "update":
            # This could be a little more complex
            print("Update recipe ingredients (feature coming soon")
        elif action == "search":
            name = click.prompt("What's the recipe name")
            recipeExists = cookBook.searchRecipe(name)
            if recipeExists:
                print("Found recipe")
            else:
                print("Could not find recipe")
        else:
            print("Invalid action")
    elif target == 'pantry':
        if action == "add":
            housePantry.addIngredients()
        elif action == "delete":
            housePantry.deleteIngredients()
        elif action == "clear":
            print("Clear all ingredients (feature coming soon)")
            #isVerified = click.prompt("Are you sure you want to clear? [y]/[n]")
    elif target == "schedule":
        if action == "add":
            weekSchedule.addRecipes()
        elif action == "delete":
            weekSchedule.deleteRecipes()
        elif action == "print":
            weekSchedule.printRecipes()
    elif target == "grocery":
        if action == "print":
            print("This is where the important function goes")

    elif target == 'exit':
        # Terminate program
        return target

    main()


if __name__ == '__main__':

    main()