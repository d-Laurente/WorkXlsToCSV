#import Prices
#import Description
from Prices import *

class Book:

    # initialiser / instance attributes
    def __init__ (self, isbn, description, image, barcode, prices):
        self.__isbn = isbn
        self.__description = description
        self.__image = image    # just a path provided in our server
        self.__barcode = barcode # path provided in server
        self.__prices = prices

    @property
    def getIsbn(self):
        return self.__isbn

    @property
    def getPrices(self):
        return self.__prices

if __name__ == '__main__':
    p1 = Prices(20.00)
    # note the description, barcode and image not represented liek this
    b = Book("9789123456789", "this is a description", "img", "barcode", p1)
    print(p1)
    print(b.getPrices)
    print(str(b.getPrices.getNet))

    