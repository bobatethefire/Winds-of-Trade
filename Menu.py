import libtcodpy as libtcod
##import Player
import Object
import textwrap

###Defines the Menu Class
class Menu():

    def __init__(self,title):
        self.title = title

    def __repr__(self):
        return "This is the "+self.title+" Menu"

    ##Draw the menu
    ##Default method incase subclass doesn't have it
    def draw(self,info):
        libtcod.console_set_default_foreground(console, libtcod.white)
        libtcod.console_print_ex(console, 0, 0, libtcod.BKGND_NONE,libtcod.LEFT,self.title)
    ##Handles the input for a given menu, given a key_press
    ##Default method incase subclass doesn't need it    
    def handle_input(self,key_press,info):
        
        return "None"
    
###Main Map that you see during gameplay
class Overview_Map_Menu(Menu):

    def __init__(self):

        Menu.__init__(self,"Overview Map")
    #Overide
    def draw(self,console,info):
        player = info["Player"]
        libtcod.console_set_default_foreground(console, libtcod.white)

        libtcod.console_print_ex(console,0,0, libtcod.BKGND_NONE, libtcod.LEFT,player.name)
        libtcod.console_print_ex(console,0,1, libtcod.BKGND_NONE, libtcod.LEFT,"--------------------")
        libtcod.console_print_ex(console,0,2, libtcod.BKGND_NONE, libtcod.LEFT,str(player.money)+"G")
        libtcod.console_print_ex(console,0,47, libtcod.BKGND_NONE, libtcod.LEFT,"k: Look")
        libtcod.console_print_ex(console,0,48, libtcod.BKGND_NONE, libtcod.LEFT,"i: Check Inventory")
        libtcod.console_print_ex(console,0,49, libtcod.BKGND_NONE, libtcod.LEFT,"r: Check Routes")
    #Overide
    def handle_input(self,key_press,info):
        if key_press == 'i':
            return "Inventory"
        elif key_press == 'k':
            return "Look"
    
###The inventory of the player
class Inventory_Menu(Menu):

    def __init__(self):
        Menu.__init__(self,"Inventory")
        
    #Overide
    def draw(self,console,info):
        player = info["Player"]
        libtcod.console_set_default_foreground(console, libtcod.white)

        sorted_Items = sorted(player.inventory.keys())
        #Display Header
        libtcod.console_print_ex(console, 0, 0, libtcod.BKGND_NONE,libtcod.LEFT,player.name)
        libtcod.console_print_ex(console,0,1, libtcod.BKGND_NONE, libtcod.LEFT,"--------------------")
        #Display Items and their amount in alphabetical order
        for i in range(len(sorted_Items)):
            display_String = sorted_Items[i] +": " + str(player.inventory[sorted_Items[i]])
            libtcod.console_print_ex(console,0,i+2, libtcod.BKGND_NONE, libtcod.LEFT,display_String)
    #Overide
    def handle_input(self,key_press,info):
        if key_press == 'i':
            return "Overview Map"
        
###The menu while you are looking around the overview map
class Look_Menu(Menu):

    def __init__(self):
        Menu.__init__(self,"Look")      
    #Overide
    def draw(self,console,info):
        tile_map = info["Map"]
        cursor = info["Cursor"]
        #Get the tile at the given spot
        tile = tile_map[cursor.x][cursor.y]
        #Draw the type to the side panel in its color
        libtcod.console_set_default_foreground(console,tile.color)
        libtcod.console_print_ex(console, 0, 0, libtcod.BKGND_NONE,libtcod.LEFT,tile.type)
    #Overide
    def handle_input(self,key_press,info):
        #Extract the info
        tile_map = info["Map"]
        cursor = info["Cursor"]

        #Exiting the Menu
        if key_press == 'k':
            return "Overview Map"

        if key_press == "KEY_UP":
            cursor.move(0,-1)
        elif key_press == "KEY_DOWN":
            cursor.move(0,1)
        elif key_press == "KEY_LEFT":
            cursor.move(-1,0)
        elif key_press == "KEY_RIGHT":
            cursor.move(1,0)
        if tile_map[cursor.x][cursor.y].type == "City":
            return "City"
###The menu present when you look at a city
class City_Menu(Menu):

    def __init__(self,):
        Menu.__init__(self,"City")

    #Overide
    def draw(self,console,info):
        city = info["City"]
        
        libtcod.console_set_default_foreground(console, libtcod.red)

        #Get relivent information
        name = city.name
        description_list = textwrap.wrap(city.description,20)
        d_len = len(description_list)
        pop = city.population 
        
        #Writes the city
        libtcod.console_print_ex(console, 0, 0, libtcod.BKGND_NONE,libtcod.LEFT,name)
        libtcod.console_print_ex(console, 0, 1, libtcod.BKGND_NONE,libtcod.LEFT,"--------------------")
        #Writes the description
        for i in range(d_len):        
            libtcod.console_print_ex(console, 0, 2+i, libtcod.BKGND_NONE,libtcod.LEFT,description_list[i])
        #Writes the population
        libtcod.console_print_ex(console, 0, d_len+3, libtcod.BKGND_NONE,libtcod.LEFT,'Population: '+str(pop))

        libtcod.console_print_ex(console, 0, d_len+4, libtcod.BKGND_NONE,libtcod.LEFT,"--------------------")
        libtcod.console_print_ex(console, 0, d_len+5, libtcod.BKGND_NONE,libtcod.LEFT,"Press # to interact:")
        for i in range(len(city.buildings)):
            libtcod.console_print_ex(console, 0, d_len+6+i, libtcod.BKGND_NONE,libtcod.LEFT,str(i+1)+": "+city.buildings[i].type)
    #Overide
    def handle_input(self,key_press,info):
        cursor = info["Cursor"]
        buildings = info["City"].buildings
        
        #Moving the cursor will change it back to the look menu
        if key_press == "KEY_UP":
            cursor.move(0,-1)
            return "Look"
        elif key_press == "KEY_DOWN":
            cursor.move(0,1)
            return "Look"
        elif key_press == "KEY_LEFT":
            cursor.move(-1,0)
            return "Look"
        elif key_press == "KEY_RIGHT":
            cursor.move(1,0)
            return "Look"

        #Is key press a number and is it non-zero, the
        #only invalid number
        if key_press.isDigit() and key_press != '0':
            building_String = buildings[int(key_press)-1].type
            return building_String

class Market_Menu(Menu):

    def __init__(self):
        Menu.__init__(self,"Market")
    #Overide
    def draw(self,console,info):

        #Get the market object
        market = info["City"].buildings[0]
        market_display = market.GUI_info
        #Draw it
        libtcod.console_set_default_foreground(console, libtcod.red)
        for i in range(len(market_display)):
            libtcod.console_print_ex(console, 0, i, libtcod.BKGND_NONE,libtcod.LEFT,market_display[i])
    #Overide
    def handle_input(self,key_press,info):

        pass
            
        
                
##Helper function to load all the neccescary menus for the main function
def load_menus():
    return {"Overview Map":Overview_Map_Menu(),
            "City":City_Menu(),
            "Inventory":Inventory_Menu(),
            "Look":Look_Menu(),
            "Market":Market_Menu()}
    
        


