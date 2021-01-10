from Client import Client
from Auto import Auto

class Case:

    def __init__(self, id, client, auto, dateout, datereturn):
        self.setID(id)
        self.setAuto(auto)
        self.setClient(client)
        self.setDateOut(dateout)
        self.setDateReturn(datereturn)

    def setID(self,id):             self.__id = id
    def setClient(self,client):     self.__client = client
    def setAuto(self,auto):         self.__auto = auto
    def setDateReturn(self,value):  self.__datereturn = value
    def setDateOut(self,value):     self.__dateout = value

    def getID(self):                return self.__id
    def getClient(self):            return self.__client
    def getAuto (self):             return self.__auto
    def getDateOut(self):           return self.__dateout
    def getDateReturn(self):        return self.__datereturn

    def __str__(self): 
        return "{} | {} | {} | {} | {} ".format( self.__id, self.__client.getFirstName(), self.__auto.getMark(), self.__dateout, self.__datereturn)