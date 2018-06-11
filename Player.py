import Item

class Player:

    def __init__(self,name):
        self.name = name
        self.inventory = {}
        self.money = 100

    #Add an Item to the inventory of the player
    def add_item(self,item,amount):

        if item.type in self.inventory:
            self.inventory[item.type] += amount

        else:
            self.inventory[item.type] = amount
    #Delete an Item from the inventory of the player
    def del_item(self, item, amount):
        #Make sure the item is actually in the inventory
        if item.type in self.inventory:
            self.inventory[item.type] -= amount

            #Make sure you can't have a negative amount of items
            if self.inventory[item.type] <0:
                self.inventory[item.type] = 0


