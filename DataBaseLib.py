import os.path as PH
import json as JS
import os
import sqlite3 as SQL

from Client import*
from Auto   import*
from Case   import*


# Класс, для хранения множества объектов данных в одном объекте
class DataList(list):
    def getByID(self, id):
        for item in self:
              if item.getID() == id: return item
        else: return None  


# Класс, отвечающий за базовые методы базы данных
class DataBase:

    def __init__(self):
        self.__Client   = DataList()
        self.__Auto     = DataList()
        self.__Case     = DataList()

    def Clear(self):
        self.__Client.clear()
        self.__Auto.clear()
        self.__Case.clear()

    def getClientList(self):            return self.__Client
    def getAutoList(self):              return self.__Auto
    def getCaseList(self):              return self.__Case
 
    def setClientList(self, value):     self.__Client = value
    def setAutoList(self, value):       self.__Auto   = value
    def setCaseList(self, value):       self.__Case   = value

    def setFirstName(self,value,ID):    self.__Client[ID].setFirstName(value)
    def setFatherName(self,value,ID):   self.__Client[ID].setFatherName(value)
    def setPhone(self,value,ID):        self.__Client[ID].setPhone(value)
    def setAdress(self,value,ID):       self.__Client[ID].setAdress(value)
    def setLastName(self,value,ID):     self.__Client[ID].setLastName(value)
    
    def getFirstName(self,ID):          return self.__Client[ID].getFirstName()
    def getFatherName(self,ID):         return self.__Client[ID].getFatherName()
    def getPhone(self,ID):              return self.__Client[ID].getPhone(value)
    def getAdress(self,ID):             return self.__Client[ID].getAdress()
    def getLastName(self,ID):           return self.__Client[ID].getLastName()
  
    def setMark(self,value,ID):         self.__Auto[ID].setMark(value)  
    def setTyp(self,value,ID):          self.__Auto[ID].setCaseCost(value) 
    def setCaseCost(self,value,ID):     self.__Auto[ID].setCaseCost(value)   
    def setCost(self,value,ID):         self.__Auto[ID].setCost(value)  

    def getMark(self,ID):               return self.__Auto[ID].getMark()  
    def getTyp(self,ID):                return self.__Auto[ID].getCaseCost() 
    def getCaseCost(self,ID):           return self.__Auto[ID].getCaseCost()   
    def getCost(self,ID):               return self.__Auto[ID].getCost()  

    def setClient(self,ID,value):       self.__Case[ID].setClient(value)  
    def setAuto(self,ID,value):         self.__Case[ID].setAuto(value) 
    def setDateReturn(self,ID,value):   self.__Case[ID].setDateReturn(value)
    def setDateOut(self,ID,value):      self.__Case[ID].setDateOut(value) 

    def getClient(self,ID):             return self.__Case[ID].getClient()  
    def getAuto(self,ID):               return self.__Case[ID].getAuto() 
    def getDateReturn(self,ID):         return self.__Case[ID].getDateReturn()
    def getDateOut(self,ID):            return self.__Case[ID].getDateOut() 

    def addClient(self,ObjClient): 
       for ITEM in self.__Client:
           if(ITEM.getID() == ObjClient.getID()) :  return 0
       self.__Client.append(ObjClient)

    def addAuto(self,ObjRoute): 
        for ITEM in self.__Auto:
           if(ITEM.getID() == ObjRoute.getID()) :   return 0
        self.__Auto.append(ObjRoute)

    def addCase(self, ObjVouchers): 
        for ITEM in self.__Case:
           if(ITEM.getID() == ObjVouchers.getID()): return 0
        self.__Case.append(ObjVouchers)

    def removeClient(self,ID): 
        for ITEM in self.__Client:
            if(ITEM.getID() == ID): 
                for I in self.__Case:
                    if(I.getClient() == ITEM):  print("ERROR: Ошибка удаления"); return 0
                self.__Client.pop(ITEM.getID() - 1); return 0
       
    def removeAuto(self,ID): 
        for ITEM in self.__Auto:
            if(ITEM.getID() == ID):
                for I in self.__Case:
                    if(I.getAuto() == ITEM):    print("ERROR: Ошибка удаления"); return 0
                self.__Auto.pop(ITEM.getID() - 1); return 0

    def removeCase(self, ID): 
        for ITEM in self.__Case:
            if(ITEM.getID() == ID): self.__Case.pop(ITEM.getID()); return 0

# Класс работы с JSON файлами
class DataBase_JSON(DataBase):

    def ReadFile(self, FileName):

        if FileName == "": print("\t --- ВЫ НЕ ВВЕЛИ НАЗВАНИЕ ФАЙЛА!!!"); return 0

        try: 
            with open(FileName) as Files: Data = JS.load(Files)

            for item in Data["Clients"]:
                Cl = Client(item["ID"], item["FirstName"], item["FatherName"], item["Phone"], item["Adress"], item["LastName"])
                self._DataBase__Client.append(Cl)

            for item in Data["Auto"]:
                Cl = Auto(item["ID"], item["Mark"], item["Typ"], item["CaseCost"], item["Cost"])
                self._DataBase__Auto.append(Cl)

            for item in Data["Case"]:
                Cl = Case(item["ID"], self._DataBase__Client.getByID(item["Client"]), self._DataBase__Auto.getByID(item["Auto"]),  item["DateReturn"], item["DateOut"])
                self._DataBase__Case.append(Cl)

        except(FileNotFoundError):  print("\t --- ФАЙЛА НЕ СУЩЕСТВУЕТ!!!") 

    def WriteFile(self, FileName): 

        if FileName == "": print("\t --- ВЫ НЕ ВВЕЛИ НАЗВАНИЕ ФАЙЛА!!!"); return 0 

        if FileName.endswith(".json"):

            L_Clients, L_Auto, L_Case = [], [], []

            for item in self._DataBase__Client():
                CL = {
                    "ID":           item.getID(),
                    "FirstName":    item.getFirstName(),
                    "FatherName":   item.getFatherName(),
                    "Phone":        item.getPhone(),
                    "Adress":       item.getAdress(),
                    "LastName":     item.getLastName()
                }
                L_Clients.append(CL)

            for item in self._DataBase__Auto():
                CL = {
                    "ID":           item.getID(),
                    "Mark":         item.getMark(),
                    "Typ":          item.getTyp(),          
                    "CaseCost":     item.getCaseCost(),        
                    "Cost":         item.getCost()                       
                }                                          
                L_Auto.append(CL)
            
            for item in self._DataBase__Case():
                CL = {
                    "ID":           item.getID(),                           
                    "Client":       item.getClient().getID(),             
                    "Auto":         item.getAuto().getID(),           
                    "DateReturn":   item.getDateOut(),                     
                    "DateOut":      item.getDateReturn()                
                }                                                 
                L_Case.append(CL)


            Data = {
                "Clients":  L_Clients,
                "Auto":     L_Auto,
                "Case":     L_Case
            }

            with open(FileName, "w") as Output: JS.dump(Data, Output)


# Класс работы с данными SQL 
class DataBase_SQLite(DataBase):

    def ReadFile(self, FileName):

        if FileName == "": print("\t --- ВЫ НЕ ВВЕЛИ НАЗВАНИЕ ФАЙЛА!!!"); return 0 

        MyDataBase = SQL.connect(FileName)
        SQLite = MyDataBase.cursor()

        for ITEM in SQLite.execute("SELECT * FROM Client"):     
            CL = Client(int(ITEM[0]),ITEM[1],ITEM[2],ITEM[3],ITEM[4],ITEM[5])
            self._DataBase__Client.append(CL)
        
        for ITEM in SQLite.execute("SELECT * FROM Auto"):      
            CL = Auto(int(ITEM[0]),ITEM[1],ITEM[2],ITEM[3],ITEM[4])
            self._DataBase__Auto.append(CL)
        
        for ITEM in SQLite.execute("SELECT * FROM Cases"):   
            CL = Case(int(ITEM[0]),self._DataBase__Client.getByID(int(ITEM[1])),self._DataBase__Auto.getByID(int(ITEM[2])),ITEM[3],ITEM[4])
            self._DataBase__Case.append(CL)


    def WriteFile(self, FileName): 

        if FileName == "": print("\t --- ВЫ НЕ ВВЕЛИ НАЗВАНИЕ ФАЙЛА!!!"); return 0 

        MyDataBase = SQL.connect(FileName)
        SQLite = MyDataBase.cursor()

        SQLite.execute("""CREATE TABLE IF NOT EXISTS Client (ID INT, FirstName TEXT, FatherName TEXT, LastName TEXT, Phone TEXT, Adress TEXT )""")
        SQLite.execute("""CREATE TABLE IF NOT EXISTS Auto   (ID INT, Mark TEXT, Typ TEXT, CaseCost TEXT, Cost TEXT)""")
        SQLite.execute("""CREATE TABLE IF NOT EXISTS Cases   (ID INT, Client INT, Auto INT, DateReturn TEXT, DateOut TEXT)""")

        MyDataBase.commit()

        MyClietn    = [ [
            self._DataBase__Client()[I].getID(),
            self._DataBase__Client()[I].getFirstName(),
            self._DataBase__Client()[I].getFatherName(),
            self._DataBase__Client()[I].getLastName(), 
            self._DataBase__Client()[I].getPhone(),
            self._DataBase__Client()[I].getAdress()
            ] for I in range(len(self._DataBase__Client())) ]


        MyAuto     = [ [
            self._DataBase__Auto()[I].getID(),
            self._DataBase__Auto()[I].getMark(),
            self._DataBase__Auto()[I].getCaseCost(),
            self._DataBase__Auto()[I].getCost(), 
            self._DataBase__Auto()[I].getTyp()
            ] for I in range(len(self._DataBase__Auto())) ] 
        
        MyCase  = [ [
            self._DataBase__Case()[I].getID(),
            self._DataBase__Case()[I].getClient().getID(),
            self._DataBase__Case()[I].getAuto().getID(),
            self._DataBase__Case()[I].getDateReturn(), 
            self._DataBase__Case()[I].getDateOut()
            ] for I in range(len(self._DataBase__Case())) ]

        for ID in range(len(MyClietn)): 
            SQLite.execute(f"SELECT ID FROM Client WHERE ID = {MyClietn[ID][0]}")
            if SQLite.fetchone() is None:
                SQLite.execute(f"INSERT INTO Client VALUES ( {MyClietn[ID][0]}, '{MyClietn[ID][1]}', '{MyClietn[ID][2]}', '{MyClietn[ID][3]}', '{MyClietn[ID][4]}', '{MyClietn[ID][5]}')")
            MyDataBase.commit()

        for ID in range(len(MyAuto)): 
            SQLite.execute(f"SELECT ID FROM Auto WHERE ID = {MyAuto[ID][0]}")
            if SQLite.fetchone() is None:
                SQLite.execute(f"INSERT INTO Auto VALUES ( {MyAuto[ID][0]}, '{MyAuto[ID][1]}', '{MyAuto[ID][2]}', '{MyAuto[ID][3]}', '{MyAuto[ID][4]}')")
            MyDataBase.commit()

        for ID in range(len(MyCase)):
            SQLite.execute(f"SELECT ID FROM Cases WHERE ID = {MyCase[ID][0]}")
            if SQLite.fetchone() is None:
                SQLite.execute(f"INSERT INTO Cases VALUES ( {MyCase[ID][0]}, {MyCase[ID][1]}, {MyCase[ID][2]}, '{MyCase[ID][3]}', '{MyCase[ID][4]}')")
            MyDataBase.commit()
    
    