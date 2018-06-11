import libtcodpy as libtcod
import EventHandler as E
import random
import Tiles
import Cities
import Object
import Player
import Item
import Building
import Menu
 
#actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

MAP_HEIGHT = 50
MAP_WIDTH = 60
 
LIMIT_FPS = 20  #20 frames-per-second maximum

VERSION = 'Pre-ALPHA 0.2'
            
##Generates a map based on given parameters
def create_map():
    #Create The Map

    #Global Variables Created
    global continent_map
    continent_map = [[ Tiles.Tile("Ocean")
        for y in range(MAP_HEIGHT) ]
            for x in range(MAP_WIDTH) ]

    global cities
    cities = []

    #Generate Contents in Map
    generate_land()
    generate_cities()
    
##Generates the land masss
##Currently just generates a square island
def generate_land():
    randX = random.randint(10,50)
    randY = random.randint(10,40)

    for x in range(randX,randX+10):
        for y in range(randY, randY+10):
            continent_map[x][y].type = "Land"

##Generates cities to the defined landmass
##Scan line method currently
def generate_cities():
    #What direction will the guesses go
    direction = random.randint(0,1)
    if direction == 0:
        direction = -1
        
    yGuess = MAP_HEIGHT/2
    xGuess = 10

    #WHILE the checked spot isn't water, thus not a valid city location
    while continent_map[xGuess][yGuess].type!="Land":
        xGuess+=1
        if xGuess> MAP_WIDTH-10:
            xGuess = 10
            yGuess+=direction
            #Making sure we don't go out of bounds
            if yGuess > 49:
                yGuess = MAP_HEIGHT/2 - 1
                direction = -1
            elif yGuess < 0:
                yGuess = MAP_HEIGHT/2 + 1
                direction = 1
                

    #We have found a place to put a city, so lets put one there
    continent_map[xGuess][yGuess].type = "City"
    #Generate the city, and add it to the list
    city = Cities.City(200)
    cities.append(city)    

##Draws the Right Info Panel
def draw_GUI():
    global GUI_info
    
    current_menu.draw(side_panel,GUI_info)

    #Blit the contents to the root console
    libtcod.console_blit(side_panel, 0,0,SCREEN_WIDTH-MAP_WIDTH,SCREEN_HEIGHT, 0,MAP_WIDTH,0)

##Render all the parts to the screen
##Currently: Map Level->Objects->GUI
def render_all():

    #draw the map
    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
                continent_map[x][y].draw(con,x,y)
 
    #draw all objects in the list
    if draw_cursor:
        cursor.draw(con)
 
    #blit the contents of "con" to the root console
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

    #Render the left GUI Panel
    libtcod.console_set_default_background(side_panel,libtcod.black)
    libtcod.console_clear(side_panel)
    draw_GUI()
    
##Handles all the input from the event handler
##Right now controls how they are handled
def handle_keys():

    global GUI_info
    global current_menu
    global draw_cursor
    #Gets current menu to make sure we haven't tryed to change
    menu_string = current_menu.title
    
    key = libtcod.console_check_for_keypress()  #real-time
 
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game
    
    #Handle the key press with the Event Handler
    key_press = E.return_key()
    #Pass that to the menu to figure out what to do with it
    menu_string = current_menu.handle_input(key_press,GUI_info)
    #Should we render the cursor?
    if current_menu.title == "Look" or current_menu.title == "City":
        draw_cursor = True
    else:
        draw_cursor = False

    #Do we need to change our menu? Also check to make sure its not a null pointer
    if menu_string != current_menu.title and menu_string is not None :
        current_menu = menus[menu_string]
           
 
#############################################
# Initialization & Main Loop
#############################################

#Create the main screen and define the main console
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Winds of Trade '+VERSION, False)
libtcod.sys_set_fps(LIMIT_FPS)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

#Defining the left panel that is used for the Menus
side_panel = libtcod.console_new(SCREEN_WIDTH-MAP_WIDTH,SCREEN_HEIGHT)
 
#Creating the cursor object
cursor_location = [0,0]
cursor = Object.Object(cursor_location[0],cursor_location[1],'X',libtcod.yellow)
draw_cursor = False

#Creating All the Menus that we will need
menus = Menu.load_menus()
current_menu = menus["Overview Map"]

#Creates instance of the player class
player = Player.Player("Danny Sexbang")

#TESTING adding items and displaying them
player.add_item(Item.Apple(50,"Mich."),10)

#Create Map
create_map()

#Create Info needed for the GUI
GUI_info = {"Player":player,
            "Map":continent_map,
            "City":cities[0],
            "Cursor":cursor}


while not libtcod.console_is_window_closed():
 
    #render the screen
    render_all()
    libtcod.console_flush()
 
    #erase all objects at their old locations, before they move
    if draw_cursor:
        cursor.clear(con)
 
    #handle keys and exit game if needed
    
    exit = handle_keys()
    if exit:
        break
