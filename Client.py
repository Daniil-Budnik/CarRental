class Client:

    def __init__(self, id, firstName, lastName, fatherName, adress, phone):
        self.setID(id)
        self.setFirstName(firstName)
        self.setLastName(lastName)
        self.setFatherName(fatherName)
        self.setAdress(adress)
        self.setPhone(phone)

    def setID(self,id):                 self.__id = id
    def setFirstName(self,firstName):   self.__firstName = firstName
    def setFatherName(self,fatherName): self.__fatherName = fatherName
    def setLastName(self,lastName):     self.__lastName = lastName
    def setPhone(self, phone):          self.__phone = phone
    def setAdress(self, adress):        self.__adress = adress
    
    def getID(self):                    return self.__id
    def getFirstName(self):             return self.__firstName
    def getFatherName (self):           return self.__fatherName
    def getLastName(self):              return self.__lastName
    def getPhone (self):                return self.__phone
    def getAdress(self):                return self.__adress


    def __str__(self):  return "{} | {} | {} | {} | {} | {}".format(self.__id, self.__firstName, self.__lastName, self.__fatherName, self.__adress, self.__phone)
