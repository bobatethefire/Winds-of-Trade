#Any header information might go here
import random as r
import Building
import Item


namelist = ['Montgomery','Juneau',
'Phoenix','Columbus','Pooptown USA']

descriptionlist = ['A small town with a great music scene',
                   'A port where only the roughest can survive',
                   'A farmtown where they take basketball seriously',
                   'A major trading city full of goods']

class City:
    ###
    #Holds the information within a city
    ###
    def __init__(self, population):
        self.population = population
        self.name = generate_name()
        self.buildings = generate_buildings()
        self.description = generate_description()      

    ##Returns information usefull to know
    def info(self):
        return_info = {self.name,self,description,self.population,self.buildings}
        return return_info

##Generates a name based on a variety of influences
##including local geography, size, and direction on continent
##Currently just a random name from a list
def generate_name():
    return namelist[r.randint(0,len(namelist)-1)]

##Generates a description of the city, of which you can
##get information that lets you know what the city is about
##Currently just a random description from a list
def generate_description():
    return descriptionlist[r.randint(0,len(descriptionlist)-1)]

##Generates buildings for the city
##Currently just adds a market
def generate_buildings():
    return [Building.Market({Item.Apple(50,"Mich."):10})]
    
