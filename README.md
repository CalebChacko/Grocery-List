# Grocery-List

This project allows users to receive an automated grocery list based on what the user would like to cook on any given week.

For the program to construct a list, three inputs must be added.

1. Recipes with Ingredients
2. All Ingredients stored at home
3. The Recipes the user would like to cook for the week

Once these three things are inputted, the user can enter one command and the list will be printed out.

### Interactive Shell Input Syntax
To enter a command, two parameters must be entered. The first is `target` and the second is `action`.

The `target` parameter is used to detail where the command will be running. The `action` parameter is used to detail what will happen at the target location.

All current targets:
* recipe - stores Recipes with Ingredients
* pantry - tracks the Ingredients stored in user's home
* schedule - tracks the Recipes for the week
* grocery - operates the grocery list
* help - provide useful instructions to user
* exit - close the application

##### Recipe Actions
Currently, the only active actions for `recipe` are `add` and `delete`. 
When adding a recipe, the user will be prompted to insert the name of the recipe and then the ingredients.
```
Target: recipe
Action: add
What's the recipe name: Cake
Add an ingredient and press enter. If finished type in '---' and enter
Milk
Butter
Sugar
Flour
---
```
For this cake recipe, milk, butter, sugar, and flour have been added.

To delete a recipe, the user will simply be prompted to name which recipe will be deleted
```
Target: recipe
Action: delete
What's the recipe name: Cake
Deleted Cake
```

##### Pantry Actions
The `pantry` location has two commands: `add` and `delete`
Similar to the `recipe add`, the user can write down each ingredient and then press enter to write the next ingredient.
```
Target: pantry
Action: add
Add each ingredient to the pantry by typing the name and pressing enter.
If finished type in '---' and enter

milk
flour
---
```

The same applies for the `delete` action.

##### Schedule Actions
The `schedule` target, which stores all recipes planned to be cooked for the week, has three commands: `add`, `delete`, and `print`

The `add` action is similar to the `recipe` and `pantry` add actions.
```
Target: schedule
Action: add
Add recipe to this week's schedule by typing the name and pressing enter.
If finished type in '---' and enter
Cake
Soup
Salad
---
```

The `delete` action works in a similar fashion.

The `schedule` target also allows the user to print out the recipes added so far. This can be done with `print`

##### Grocery Actions
Currently, the only action for the `grocery` target is `print list`. This gives the user the grocery list they need before cooking the recipes for the week.

### Current Version Features
* Basic Functionality 
    * Ability to create/remove recipes, pantry ingredients, and recipes from the schedule
    * Ability to print out the grocery list


### Upcoming Version Features
##### Commands/Recipes stored within text files 
At the moment, when a user adds ingredients and recipes, it is only stored while the application is open. Once closed, it is all erased.
This feature is crucial for anyone to use this long term.

##### Update existing Recipes
With this feature, an ingredient can be added/deleted from a Recipe

##### Help Target 
New text will be added to the Help Target to guide users

##### Pantry Clear
If all items needed to be removed from the user's house, this action will help the user complete the task with one word.

### Why this project?
This past summer, I returned home to my family during Covid-19. I learned how to cook lots of new recipes daily. However some days, I noticed I was missing the needed ingredients to make certain recipes.
I also had a desire to apply my knowledge of data structures from my previous school term. Thus, this project was born. I understand that applications like this exist already, but I wanted to try and build my own from scratch. With the flexibility of designing my own application, I plan to taylor it to fit the needs of my home. 

In the future, I could see this project becoming a small iOS app so I can update the `pantry` from my iPad on a fridge. Another unique feature would be to have a barcode reader that can identify the product and it's expiry date. With this feature, the application could recommend certain recipes to make sure all your almost expired ingredients are used up.

