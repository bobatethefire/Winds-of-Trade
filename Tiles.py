import libtcodpy as libtcod

class Tile:
    #a tile of the map and its properties
    def __init__(self, tileSet):
        self.type = tileSet
        #setting default types
        self.color = libtcod.black
        self.character = ' '

        
    #Draw the individual tile
    def draw(self,con,x,y): 
        #set some specifics
        if self.type == "Land":
            self.color = libtcod.green
            self.character = 'l'
        elif self.type == "Ocean":
            self.color = libtcod.blue
            self.character = 'O'
        elif self.type == "City":
            self.color = libtcod.red
            self.character = 't'

        #Draw said tile
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, x, y, self.character, libtcod.BKGND_NONE)
