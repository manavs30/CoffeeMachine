# CoffeeMachine
Simulation of multi threaded coffee machine
It has n number of outlets, given in the input json itself. Each outlet denotes a thread.
The json also has total_items_quantity denoting the ingredients and the quantity present in the machine.
The last field present in json is beverages. It shows different beverages that can be brewed in the machine and the amount of ingredients required for them.

Tested with Python 3.6.6

To run the code:
  cd CoffeeMachine/
  python3 start_machine.py test_cases/test1.json 30

The first argument is the path of input json file.
The second argument is the time required by machine to brew the beverage after acquiring the ingredients.

After running the code, it will prompt you for entering the trigger for different actions. Different triggers are:
  "n" : This is for brewing a beverage. After entering n. If the coffee machine doesn't have a free outlet, it will exit this operation. If it does have free outlet, it will show the beverage options and prompt the customer to select one.
  "g" : This shows the ingredients and their respective quantities present in the machine.
  "a" : This is for adding the ingredients to the machine. After selecting this option, customer will be prompted to select the ingredient name from given options and then value that should be added to the existing quantity of that ingredient.
  "b" : This is used to show beverages and the respective ingredients and their quantity required.
  "x" : This is used to exit the machine. It will make sure that the existing orders are fulfilled before exiting.
 
 This machine is robust enough to take different ingredients and beverages as input and work on it. There is no hard coding of ingredients and beverages in the code.
 
 If the machine sees empty information for beverages or outlets as 0, it fails to start as expected. 
 But, even if total_items_quantity has empty information it still starts as we can use "a" operation to add different ingredients to the machine.
