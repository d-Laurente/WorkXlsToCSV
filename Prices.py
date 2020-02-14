class Prices:

    def __init__(self, wasPrice):
        self.__wasPrice = wasPrice
        self.__netPrice = 0.5 * wasPrice
        self.__specialPrice = 0.4 * wasPrice

    def setWasPrice(self, wasPrice):
        self.__wasPrice = wasPrice
        self.__netPrice = 0.5 * wasPrice
        self.__specialPrice = 0.4 * wasPrice

    def setNetPrice(self, netPrice):
        self.__netPrice = netPrice

    def setSpecialPrice(self, specialPrice):
        self.__specialPrice = specialPrice

    @property
    def getWas(self):
        return self.__wasPrice

    @property
    def getNet(self):
        return self.__netPrice
    
    @property
    def getSpecial(self):
        return self.__specialPrice
    
    def __str__(self):
        return "was price: " + str(self.__wasPrice) + "\t\t net price: " + str(self.__netPrice) + "\t special: " + str(self.__specialPrice)
        