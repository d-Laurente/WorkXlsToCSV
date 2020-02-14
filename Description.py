class Description:
    
    def __init__(self, name):
        self.__name = name
        self.__blurb = ""
        self.__pages = 0
        self.__dimensions = "0 x 0"
        self.__coverType = ""
        self.__publisher = ""
        self.__yearPublished = ""

    def setName(self, name):
        self.__name = name
    
    def setBlurb(self, blurb):
        self.__blurb = blurb

    def setPages(self, pages):
        self.__pages = pages

    def setDimensions(self, dimensions):
        self.__dimensions = dimensions

    def setCoverType(self, coverType):
        self.__coverType = coverType

    def setPublisher(self, publisher):
        self.__publisher = publisher

    def setYearPublished(self, year):
        self.__yearPublished = year

    @property
    def getName(self):
        return self.__name

    @property
    def getBlurb(self):
        return self.__blurb

    @property
    def getPages(self):
        return self.__pages

    @property
    def getDimensions(self):
        return self.__dimensions

    @property
    def getCoverType(self):
        return self.__coverType

    @property
    def getPublisher(self):
        return self.__publisher

    @property
    def getYearPublished(self):
        return self.__yearPublished

    #the big function here is to download everything
    def downloadDetails():
        pass
