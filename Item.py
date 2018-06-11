
##Item Class that defines items
class Item():

    def __init__(self,baseprice,description,category,orgin):
        self.base_price = baseprice
        self.category = category
        self.type = description
        self.orgin = orgin

    def base_price_from_string(self):
        return base_price
        
##Item Category of Food
class Food(Item):

    def __init__(self,baseprice,description,orgin):
        Item.__init__(self,baseprice,description,"Food",orgin)


class Apple(Food):

    def __init__(self,baseprice,orgin):

        Food.__init__(self,10,"Apple",orgin)

class Bread(Food):

    def __init__(self,baseprice,orgin):

        Food.__init__(self,15,"Bread",orgin)
