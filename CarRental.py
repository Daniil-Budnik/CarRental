import os
import sqlite3 as SQL

from Client import*
from Auto   import*
from Case   import*

import DataBaseLib as MyBD

# Пример работы чтения и записи JSON
def Task_1():

    print("\n\t>>\tJSON\t<<\n")

    # Считываем БД с json
    BD = MyBD.DataBase_JSON()
    BD.ReadFile("MyDataBase.json")

    print("...........................................................")

    # Выводим всю информацию
    print("\n\n\t>> Клиенты: <<\n")
    for Count in BD.getClientList():    print(Count,'\n')
    
    print("\n\n\t>> Автомобили: <<\n")
    for Count in BD.getAutoList():      print(Count,'\n')
    
    print("\n\n\t>> Выданные автомобили: <<\n")
    for Count in BD.getCaseList():      print(Count,'\n')

    print("...........................................................")

# Пример работы чтения и записи SQL
def Task_2(): 

    print("\n\t>>\tSQL\t<<\n")

    # Загружаем базу данных
    BD = MyBD.DataBase_SQLite()
    BD.ReadFile("MyDataBase.db")

    print("...........................................................")

    # Выводим всю информацию
    print("\n\n\t>> Клиенты: <<\n")
    for Count in BD.getClientList():    print(Count,'\n')
    
    print("\n\n\t>> Автомобили: <<\n")
    for Count in BD.getAutoList():      print(Count,'\n')
    
    print("\n\n\t>> Выданные автомобили: <<\n")
    for Count in BD.getCaseList():      print(Count,'\n')
    
    print("...........................................................")

# Метод генерирует тестовые базы данных
def GeneratorBD():

    BD      = MyBD.DataBase()
    BD_JSON = MyBD.DataBase_JSON()
    BD_SQL  = MyBD.DataBase_SQLite()


    CLIENT = [
        Client(1,"1","1","1","1","1"),
        Client(2,"2","2","2","2","2"),
        Client(3,"3","3","3","3","3")
        ]

    AUTO = [
        Auto(1,"1","1","1","1"),
        Auto(2,"2","2","2","2"),
        Auto(3,"3","3","3","3")
        ]

    CASE = [
        Case(1,CLIENT[1],AUTO[2],"1","1"),
        Case(2,CLIENT[2],AUTO[0],"2","2"),
        Case(3,CLIENT[0],AUTO[1],"3","3")
        ]

    BD.addClient(CLIENT[0]);    BD.addClient(CLIENT[1]);    BD.addClient(CLIENT[2])
    BD.addAuto(AUTO[0]);        BD.addAuto(AUTO[1]);        BD.addAuto(AUTO[2])
    BD.addCase(CASE[0]);        BD.addCase(CASE[1]);        BD.addCase(CASE[2])

    BD_JSON.setClientList(BD.getClientList)
    BD_JSON.setAutoList(BD.getAutoList)
    BD_JSON.setCaseList(BD.getCaseList)
    
    BD_JSON.WriteFile("MyDataBase.json")

    BD_SQL.setClientList(BD.getClientList)
    BD_SQL.setCaseList(BD.getCaseList)
    BD_SQL.setAutoList(BD.getAutoList)
    
    BD_SQL.WriteFile("MyDataBase.db")


def Main():

    print("\n\t>>\tHELLO WORLD\t<<\n")

    GeneratorBD()  # Генерирует тестовые данные
    Task_1()       # Пример работы чтения и записи JSON
    Task_2()       # Пример работы чтения и записи SQL

# --------------------------------------------------------------------------------------------------

if __name__ == "__main__": Main()

# --------------------------------------------------------------------------------------------------
