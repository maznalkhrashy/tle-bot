import os
import sqlite3

class Givt:
    def Add(self,id,pont10,pont100,pont1000):
        with sqlite3.connect("dbs/data.db") as connection:	
            cursor = connection.cursor()
            print(f"INSERT INTO givt VALUES ('{id}','{pont10}','{pont100}','{pont1000}'")
            cursor.execute(f"INSERT INTO givt VALUES ('{id}','{pont10}','{pont100}','{pont1000}')")	
            
            connection.commit()

    def Get(self,id):
        with sqlite3.connect("dbs/data.db") as connection:	
            cursor = connection.cursor()	
            DataUser = cursor.execute('SELECT * FROM givt WHERE id=?', (f"{id}",)).fetchall()
            connection.commit()
            return DataUser[0]
class data:
    def __init__(self):
        if not os.path.isfile("dbs/data.db"):
            with sqlite3.connect("dbs/data.db") as connection:
                cursor = connection.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS dataID (id TEXT,user TEXT)")	
                cursor.execute("CREATE TABLE IF NOT EXISTS orders (id TEXT,stack TEXT)")	
                cursor.execute("CREATE TABLE IF NOT EXISTS givt (id TEXT, pont10 TEXT,pont100 TEXT, pont1000 TEXT)")
                connection.commit()
    def Add(self,id,chat):
        
        with sqlite3.connect("dbs/data.db") as connection:	
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO dataID VALUES ('{id}','{chat}')")	
            connection.commit()

    def Get(self,id):
        list = []
        with sqlite3.connect("dbs/data.db") as connection:	
            cursor = connection.cursor()	
            DataUser = cursor.execute('SELECT * FROM dataID WHERE id=?', (f"{id}",)).fetchall()
            connection.commit()
            for i in DataUser:
                list.append(i[1])
            
            return list
    def de(self,id):
        with sqlite3.connect("dbs/data.db") as connection:
            cursor = connection.cursor()
            cursor.execute('DELETE from dataID where id=?', (id,)).fetchall()
            connection.commit()

class statck:
    def Add(self,id,st):  
        print(id)  
        with sqlite3.connect("dbs/data.db") as connection:	
            cursor = connection.cursor()
            DataUser = cursor.execute('SELECT * FROM orders WHERE id=?', (f"{id}",)).fetchall()
            if DataUser == []:
                print("1")
                cursor.execute(f"INSERT INTO orders VALUES ('{id}','{st}')")
                connection.commit()
            else:
                print("2")
                print(st)
                cursor.execute('UPDATE orders SET stack=? WHERE id=?',(st,id,))
                
                connection.commit()
               
            
    def Get(self,id):
        with sqlite3.connect("dbs/data.db") as connection:	
            cursor = connection.cursor()	
            DataUser = cursor.execute('SELECT * FROM orders WHERE id=?', (id,)).fetchall()
            connection.commit()
            return DataUser[0][1]
    def DefAdd(self,id,stack):
        with sqlite3.connect("dbs/data.db") as connection:			
            cursor = connection.cursor()
            cursor.execute(f"UPDATE orders SET stack= {stack} WHERE id='{id}'")
            connection.commit()
            