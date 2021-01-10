class Auto:

    def __init__(self, id,  mark, cost, caseCost, typ):
        self.setID(id)
        self.setMark(mark)
        self.setCaseCost(caseCost)
        self.setTyp(typ)
        self.setCost(cost)

    def setID(self, id):            self.__id = id
    def setMark(self, mark):        self.__mark = mark
    def setTyp(self,typ):           self.__typ = typ
    def setCaseCost(self,caseCost): self.__caseCost = caseCost
    def setCost(self, cost):        self.__cost = cost

    def getID(self):                return self.__id
    def getMark(self):              return self.__mark
    def getCaseCost (self):         return self.__caseCost
    def getCost(self):              return self.__cost
    def getTyp(self):               return self.__typ

    def __str__(self): return "{} | {} | {} | {} | {}".format(  self.__id, self.__mark, self.__cost, self.__caseCost, self.__typ)

