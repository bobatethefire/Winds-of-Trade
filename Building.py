import Item


###Class to define what a building is
class Building():

    def __init__(self,description):
        self.type = description

        ##Default sting for the generic building
    def GUI_info(self):
        return self.type


###Defines what a market is and how it will function
###Subclass of: Building
class Market(Building):

    def __init__(self,inventory):
        self.inventory = inventory
        Building.__init__(self,"Market")

    ##Returns a list of strings to display on the GUI
    def GUI_info(self):
        #Starts with the header and a spacer
        return_list = ["  Item  | #  | $  ",
                       "--------------------"]

        sorted_Items = sorted(self.inventory.keys())

        for i in range(len(sorted_Items)):
            item = sorted_Items[i].type
            #Create the spaces for centering Items
            item_spaces = " "*(8-len(item))

            amount = self.inventory[sorted_Items[i]]
            amount_spaces = " "*(4-len(str(amount)))

            price = sorted_Items[i].base_price

            display_String = item+item_spaces+"|"+str(amount)+amount_spaces+"|"+str(price)

            return_list.append(display_String)


        return return_list
