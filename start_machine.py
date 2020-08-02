from machine import Machine
from thread_pool import ThreadPool
import traceback
import sys

def main(json_file_path, time_for_making_beverage):
    print(time_for_making_beverage)
    my_machine = Machine(json_file_path, int(time_for_making_beverage))
    my_thread_pool = ThreadPool(my_machine)

    while True:
        print("Press n to get a new beverage. Press g to get info about all items. Press a to add more quantity for items. Press b to get info about all beverages. Press x to exit.")
        inp = input()
        if inp=="x":
            break
        elif inp=="g":
            print("Items in machine are: {}".format(my_machine.item_dict_getter()))
        elif inp=="n":
            #We are checking if any outlet is available to take our request
            if my_thread_pool.isPoolAvailable():
                beverages = my_machine.beverages_keys_getter()
                print("Your options for beverages are : {}".format(beverages))
                name = input("INPUT NEW BEVERAGE ")
                if name not in beverages:
                    print("Wrong beverage name {}".format(name))
                else:
                    my_thread_pool.make_beverage(name)
            else:
                print("All the outlets are busy brewing beverages. Wait for some time.")
        elif inp=="a":
            items = my_machine.items_keys_getter()
            print("Your options for items are : {}".format(items))
            name = input("INPUT NAME OF ITEM ")
            if name not in items:
                print("Wrong item name {}".format(name))
            else:
                val = input("INPUT VALUE OF ITEM ")
                try:
                    val = int(val)
                    my_machine.update_items_repo(name, val)
                except ValueError:
                    print("Value provided is not an integer")
        elif inp=="b":
            print("Ingredients required for beverages are: {}".format(my_machine.beverages_dict_getter()))
        else:
            print("Wrong input")

if __name__ == '__main__':
   try:
      main(sys.argv[1], sys.argv[2])
      sys.exit(0)
   except Exception:
      traceback.print_exc(file=sys.stderr)
      sys.exit(1)
