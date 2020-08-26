import click
from recipe import Recipe
from recipebook import RecipeBook

cookBook = RecipeBook()

@click.command()
@click.option("--target", prompt=True, help="Add to target location")
@click.option("--action", prompt=True, help="Add to target location")
def main(target, action):
    cookBook.name = "This is mine"
    if target == 'recipe':
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
            print("Update")
        elif action == "search":
            name = click.prompt("What's the recipe name")
            recipeExists = cookBook.searchRecipe(name)
            if recipeExists:
                cookBook.deleteRecipe(name)
            else:
                print("Could not find recipe")
        else:
            print("Invalid action")
    elif target == 'pantry':
        print("I'm a pantry")
    elif target == 'exit':
        # Terminate program
        return target

    main()


if __name__ == '__main__':

    main()