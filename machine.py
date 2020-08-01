import json
import time

class Machine(object) :

    def __init__(self, json_file, time_for_making_beverage):
        print("Setting up Coffee Machine..")
        #Init function stores outlets_count, items_dictionary and beverages_dictionary in class variables
        self.outlets_count, self.items_dict, self.beverages_dict = self.__get_info_from_json(json_file)
        if self.outlets_count <= 0:
            raise Exception("Invalid Outlets Count")
        if self.beverages_dict is None or len(self.beverages_dict)==0:
            raise Exception("No beverages found")
        #Storing list of beverages to show in UI
        self.beverages_keys = self.beverages_dict.keys()
        self.items_keys = self.get_all_item_keys()
        #We will sleep for this amount of time after acquiring the required ingredients to brew our beverage
        self.time_for_making_beverage = time_for_making_beverage

    #Private method to convert json to required info
    def __get_info_from_json(self, json_file):
        with open(json_file) as handle:
            dictdump = json.loads(handle.read())
        return dictdump["machine"]["outlets"]["count_n"], dictdump["machine"]["total_items_quantity"], dictdump["machine"]["beverages"]

    #This function will get all the items present in items and also fetch items from each beverage to add unique items to the list
    #We are running this only once while inititating the machine, so not a big deal.
    def get_all_item_keys(self):
        #We are using set, so as to have only unique items
        keys = set(self.items_dict.keys())
        for beverage in self.beverages_keys:
            more_keys = (self.beverages_dict[beverage].keys())
            keys.update(more_keys)
        return keys

    def outlets_getter(self):
        return self.outlets_count

    def beverages_dict_getter(self):
        return self.beverages_dict

    def beverages_keys_getter(self):
        return self.beverages_keys

    def item_dict_getter(self):
        return self.items_dict

    def items_keys_getter(self):
        return self.items_keys

    def update_items_repo(self, key, value):
        if key not in self.items_dict:
            self.items_dict[key] = value
        else:
            self.items_dict[key] += value

    def make_beverage(self, beverage_name, lock):
        print("MAKING BEVERAGE {}".format(beverage_name))
        #Updating the value for items under the lock to maintain consistency
        with lock:
            value_to_be_reduced = {}
            for item_name, value in self.beverages_dict[beverage_name].items():
                #This is the case when item is there in beverage dict but not present in our items dict
                if item_name not in self.items_dict:
                    print("Unable to make beverage {} because item {} not available".format(beverage_name, item_name))
                    return
                #This is the case when item is there in beverage dict, but enough quantity is not present in items dict
                elif self.items_dict[item_name] < self.beverages_dict[beverage_name][item_name]:
                    print("Unable to make beverage {} because item {} not sufficient".format(beverage_name, item_name))
                    return
                else:
                    value_to_be_reduced[item_name] = value

            for item_name, value in value_to_be_reduced.items():
                new_value = self.items_dict[item_name] - value
                self.items_dict[item_name] = new_value
        #Waiting to get our beverage ready
        time.sleep(self.time_for_making_beverage)
        print("BEVERAGE {} IS READY".format(beverage_name))
