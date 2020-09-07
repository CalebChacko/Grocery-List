import click
from groceryList import GroceryList
from recipebook import RecipeBook
from pantry import Pantry
from schedule import Schedule
from taskmanager import Manager

gList = GroceryList()
cookBook = RecipeBook()
housePantry = Pantry()
weekSchedule = Schedule()

manager = Manager()

@click.command()
@click.option("--target", prompt=True, help="Add to target location")
@click.option("--action", prompt=True, help="Add action to target location")
def main(target, action):

    if target == 'recipe':
        manager.RecipeBookManager(cookBook, action)
    elif target == 'pantry':
        manager.PantryManager(housePantry, action)
    elif target == "schedule":
        manager.ScheduleManager(weekSchedule, action)
    elif target == "grocery":
        manager.GroceryListManager(cookBook, housePantry, weekSchedule, gList, action)
    elif target == "help":
        print("Give user some info on commands")
    elif target == 'exit':
        # Terminate program
        return target

    main()

def intro():
    print("\n--------------------------------")
    print("Welcome to Grocery List Services")
    print("This application can help provide you with\na required Grocery List based on what's in your house and what you are planning to cook.")
    print("|  --Targets--  ")
    print("|  [recipe] - ")
    print("|  [pantry] - ")
    print("|  [schedule] - ")
    print("|  [grocery] - ")
    print("|  [help] - ")
    print("|  [exit] - \n")

if __name__ == '__main__':
    intro()
    main()